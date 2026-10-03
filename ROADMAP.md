# Roadmap

## Implemented

- Quarto website with thematic navigation, full-site search, local table of contents and code-copy controls.
- Public GitHub repository with an automatic Quarto-to-GitHub-Pages deployment workflow.
- A compact homepage that acts as the toolbox index.
- Standard project template with immutable raw input, persistent processed data, final output, staged QMD files and project-local `src/` functions.
- Cross-platform, dependency-free `dj-new` CLI; it validates project names, refuses overwrites and never initializes Git.
- Copy-pastable dataframe, vector and raster references in R and Python where both ecosystems are useful.
- First useful versions of statistics, text analysis and generic API references.
- Verified geo.admin STAC discovery in R and Python, including bbox/polygon search, cursor pagination, item/asset inspection, explicit download and G1/K4 guidance.
- Verified OFS municipality level, correspondence and mutation helpers with raw-response preservation and character-safe codes.
- Historical municipality harmonization with explicit split/unmatched checks, many-to-one aggregation and before/after totals.
- Verified STAT-TAB/PxWeb JSON-stat2 workflow with metadata inspection, dynamic latest periods, wide-first checks and non-destructive aggregate diagnostics.
- Tested joint-topology Mapshaper workflow with named layers, optional user-supplied simplification and output validation.
- Generic and Switzerland-oriented Datawrapper multilayer TopoJSON workflow, including projected extent anchors and pre-upload join checks.
- Small Datawrapper v3 client for draft creation, data/topology upload, metadata configuration and explicit publication, adapted from the existing working scripts.
- geo.admin STAC examples migrated to the recommended v1 endpoint.
- Verified swissSURFACE3D point-cloud and official DSM discovery, latest-per-tile selection, asset manifests and a documented PDAL tile-to-raster pipeline.
- Verified SWISSIMAGE discovery, explicit 0.1/2 m asset selection, download, GDAL mosaic and optional polygon crop.
- Verified satellite-imagery decision guide covering Copernicus, NASA Earthdata/FIRMS and Landsat, with a tested Sentinel-2 L2A STAC search and coverage ranking.
- Verified Natural Earth and Eurostat GISCO world/country geometry references with copyable R and Python access examples.
- Verified `tamMap::canton_CH()` metadata fields and kept the public canton-flag helper independent of organization-specific asset URLs.

## Next recipes

No large recipe is scheduled. Add workflows only after they recur in real projects.

## Open questions / sources to verify

- Monitor OFS municipality-service schemas and the STAT-TAB API because these external services can change independently of the toolbox.
- Monitor the versioned geo.admin STAC v1 endpoint and collection schemas; v0.9 is deprecated.
- Run a create/upload/configure smoke test against a disposable Datawrapper chart when external mutation is explicitly intended; token authentication, local code, official endpoints and an existing real output have been verified without changing an account.
- Select an approved public source for canton flag assets; keep organization-specific asset URLs out of the public repository.
- Execute and inspect the swissSURFACE3D PDAL classification/raster pipeline on one current COPC tile in a dedicated environment; installing PDAL in the current Homebrew environment would upgrade 97 unrelated dependencies.
