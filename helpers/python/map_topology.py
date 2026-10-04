"""Reusable geometry helpers for multilayer Datawrapper maps.

Source: data-toolbox helper `map-topology`.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import box


def add_extent_anchors(background_gdf, bounds, anchor_size_m=100):
    """Append two tiny polygons so a background layer carries exact bounds."""
    if background_gdf.crs is None or background_gdf.crs.is_geographic:
        raise ValueError("Use a projected CRS with metre units")
    if background_gdf.empty:
        raise ValueError("`background_gdf` is empty")
    if anchor_size_m <= 0:
        raise ValueError("`anchor_size_m` must be greater than zero")

    min_x, min_y, max_x, max_y = map(float, bounds)
    if min_x >= max_x or min_y >= max_y:
        raise ValueError("Invalid bounds")

    anchors = gpd.GeoDataFrame(
        {
            "id": ["__extent_south_west__", "__extent_north_east__"],
            "name": ["", ""],
        },
        geometry=[
            box(min_x, min_y, min_x + anchor_size_m, min_y + anchor_size_m),
            box(max_x - anchor_size_m, max_y - anchor_size_m, max_x, max_y),
        ],
        crs=background_gdf.crs,
    )

    anchored = gpd.GeoDataFrame(
        pd.concat([background_gdf, anchors], ignore_index=True),
        geometry="geometry",
        crs=background_gdf.crs,
    )

    actual_bounds = tuple(map(float, anchored.total_bounds))
    expected_bounds = (min_x, min_y, max_x, max_y)
    if any(
        abs(actual - expected) > 1e-6
        for actual, expected in zip(actual_bounds, expected_bounds)
    ):
        raise RuntimeError(f"Extent mismatch: {actual_bounds} != {expected_bounds}")

    return anchored


def build_multilayer_topology(layers, output_path, keep=None):
    """Build one TopoJSON while retaining the keys in `layers` as layer names."""
    if not shutil.which("mapshaper"):
        raise RuntimeError("Install Mapshaper with: npm install -g mapshaper")
    if not layers:
        raise ValueError("At least one layer is required")

    expected_names = list(layers)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="mapshaper-") as temp_name:
        temp_dir = Path(temp_name)
        inputs = []

        for name, gdf in layers.items():
            if not name or Path(name).name != name:
                raise ValueError(f"Invalid layer name: {name!r}")
            if gdf.crs is None:
                raise ValueError(f"Layer {name!r} has no CRS")
            if gdf.empty:
                raise ValueError(f"Layer {name!r} is empty")

            input_path = temp_dir / f"{name}.geojson"
            gdf.to_crs(4326).to_file(input_path, driver="GeoJSON")
            inputs.append(str(input_path))

        temporary_output = temp_dir / "map.topojson"
        command = ["mapshaper", "-i", *inputs, "combine-files", "-clean"]

        if keep is not None:
            keep = str(keep).strip()
            if not keep:
                raise ValueError("`keep` must be omitted or contain a Mapshaper value")
            command.extend(["-simplify", keep, "keep-shapes"])

        command.extend(["-o", str(temporary_output), "format=topojson"])
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode:
            message = result.stderr.strip() or result.stdout.strip()
            raise RuntimeError(f"Mapshaper failed: {message}")

        topology = json.loads(temporary_output.read_text(encoding="utf-8"))
        output_names = list(topology.get("objects", {}))
        if output_names != expected_names:
            raise RuntimeError(
                f"Unexpected output layers: {output_names}; expected {expected_names}"
            )

        output_path.write_text(
            json.dumps(topology, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )

    return topology


def validate_map_join(topology, layer, map_key, data, data_key):
    """Fail when data keys are duplicated or absent from a TopoJSON layer."""
    try:
        geometries = topology["objects"][layer]["geometries"]
    except KeyError as error:
        raise ValueError(f"Topology layer not found: {layer}") from error

    map_ids = []
    for geometry in geometries:
        properties = geometry.get("properties", {})
        if map_key not in properties:
            raise ValueError(f"Map key {map_key!r} is missing from layer {layer!r}")
        map_ids.append(str(properties[map_key]))

    if data_key not in data.columns:
        raise ValueError(f"Data key not found: {data_key}")

    data_ids = data[data_key].dropna().astype("string")
    duplicated = sorted(data_ids[data_ids.duplicated(keep=False)].unique().tolist())
    if duplicated:
        raise ValueError(f"Duplicated data IDs: {duplicated[:20]}")

    unmatched = sorted(set(data_ids) - set(map_ids))
    if unmatched:
        raise ValueError(f"Data IDs missing from the map: {unmatched[:20]}")

    return {
        "map_features": len(map_ids),
        "data_rows": len(data_ids),
        "unused_map_ids": sorted(set(map_ids) - set(data_ids)),
    }
