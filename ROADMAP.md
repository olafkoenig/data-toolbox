# Roadmap

## Implemented

- Quarto website with thematic navigation, full-site search, local table of contents and code-copy controls.
- A compact homepage that acts as the toolbox index.
- Standard project template with immutable raw input, persistent processed data, final output, staged QMD files and project-local `src/` functions.
- Cross-platform, dependency-free `dj-new` CLI; it validates project names, refuses overwrites and never initializes Git.
- Copy-pastable dataframe, vector and raster references in R and Python where both ecosystems are useful.
- First useful versions of statistics, text analysis and generic API references.
- Explicit holding pages for future Swiss, Datawrapper, STAC, point-cloud, orthophoto and satellite workflows.

## Next recipes

1. Verify and implement the OFS PxWeb / STAT-TAB JSON-stat workflow, including wide-first checks and explicit aggregate diagnostics.
2. Verify municipality-level and municipality-correspondence endpoints, then implement historical municipality harmonization with manual handling of true splits.
3. Implement transparent geo.admin STAC discovery: collection, date and geometry search first; asset selection and download second.
4. Document and test joint-topology Mapshaper simplification for municipalities, cantons, lakes and rivers using a user-supplied `keep` value.
5. Build generic and Switzerland-oriented multilayer TopoJSON recipes, including the Datawrapper background-extent anchor workaround.
6. Add Datawrapper API upload/configuration only after testing with credentials supplied outside the repository.
7. Build swissSURFACE3D tile discovery and a PDAL-based DEM/DSM pipeline.
8. Add SWISSIMAGE discovery, download and mosaic steps by reusing the STAC and raster patterns.
9. Expand the satellite-imagery finder with verified catalog links and a product decision table.

## Open questions / sources to verify

- Create and push the `olafkoenig/data-toolbox` remote after GitHub CLI authentication is refreshed; choose repository visibility before creation.
- Decide whether GitHub Pages should publish from a rendered branch, GitHub Actions or another established personal workflow.
- Verify current request parameters, response schemas and licensing for the OFS endpoints before adding executable code:
  - `https://sms.bfs.admin.ch/WcfBFSSpecificService.svc/AnonymousRest/communes/levels`
  - `https://sms.bfs.admin.ch/WcfBFSSpecificService.svc/AnonymousRest/communes/correspondances`
  - `https://www.agvchapp.bfs.admin.ch/api/communes/mutations`
- Verify the current PxWeb/STAT-TAB API endpoint and JSON-stat decoding behavior; do not promote legacy `/sq/` CSV URLs.
- Verify geo.admin STAC collection IDs, asset media types and date semantics, including `ch.bfs.historisierte-administrative_grenzen_g1` and `ch.bfs.historisierte-administrative_grenzen_k4`.
- Test Mapshaper commands against representative related layers to confirm shared-topology behavior and layer naming.
- Test Datawrapper extent anchors and API configuration against a real locator-map workflow.
- Confirm `tamMap::canton_CH()` availability and returned fields before adding canton metadata examples.
- Select an approved public source for canton flag assets; keep organization-specific asset URLs out of the public repository.
- Select and verify authoritative catalog/product documentation for Sentinel/Copernicus, MODIS and NASA Earth-observation products.
- Validate PDAL classification filters and raster-writer settings on current swissSURFACE3D tiles.
