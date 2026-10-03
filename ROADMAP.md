# Roadmap

## Implemented

- Quarto website with thematic navigation, full-site search, local table of contents and code-copy controls.
- Public GitHub repository with an automatic Quarto-to-GitHub-Pages deployment workflow.
- A compact homepage that acts as the toolbox index.
- Standard project template with immutable raw input, persistent processed data, final output, staged QMD files and project-local `src/` functions.
- Cross-platform, dependency-free `dj-new` CLI; it validates project names, refuses overwrites and never initializes Git.
- Copy-pastable dataframe, vector and raster references in R and Python where both ecosystems are useful.
- First useful versions of statistics, text analysis and generic API references.
- Explicit holding pages for future Swiss, Datawrapper, STAC, point-cloud, orthophoto and satellite workflows.
- Verified geo.admin STAC discovery in R and Python, including bbox/polygon search, cursor pagination, item/asset inspection, explicit download and G1/K4 guidance.

## Next recipes

1. Verify and implement the OFS PxWeb / STAT-TAB JSON-stat workflow, including wide-first checks and explicit aggregate diagnostics.
2. Verify municipality-level and municipality-correspondence endpoints, then implement historical municipality harmonization with manual handling of true splits.
3. Document and test joint-topology Mapshaper simplification for municipalities, cantons, lakes and rivers using a user-supplied `keep` value.
4. Build generic and Switzerland-oriented multilayer TopoJSON recipes, including the Datawrapper background-extent anchor workaround.
5. Add Datawrapper API upload/configuration after auditing existing scripts and testing with credentials supplied outside the repository.
6. Build swissSURFACE3D tile discovery and a PDAL-based DEM/DSM pipeline.
7. Add SWISSIMAGE discovery, download and mosaic steps by reusing the STAC and raster patterns.
8. Expand the satellite-imagery finder with verified catalog links and a product decision table.

## Open questions / sources to verify

- Verify current request parameters, response schemas and licensing for the OFS endpoints before adding executable code:
  - `https://sms.bfs.admin.ch/WcfBFSSpecificService.svc/AnonymousRest/communes/levels`
  - `https://sms.bfs.admin.ch/WcfBFSSpecificService.svc/AnonymousRest/communes/correspondances`
  - `https://www.agvchapp.bfs.admin.ch/api/communes/mutations`
- Verify the current PxWeb/STAT-TAB API endpoint and JSON-stat decoding behavior; do not promote legacy `/sq/` CSV URLs.
- Monitor the versioned geo.admin STAC 0.9 endpoint for a future API-version change; no unversioned root currently exists.
- Test Mapshaper commands against representative related layers to confirm shared-topology behavior and layer naming.
- Test Datawrapper extent anchors and API configuration against a real locator-map workflow.
- Confirm `tamMap::canton_CH()` availability and returned fields before adding canton metadata examples.
- Select an approved public source for canton flag assets; keep organization-specific asset URLs out of the public repository.
- Select and verify authoritative catalog/product documentation for Sentinel/Copernicus, MODIS and NASA Earth-observation products.
- Validate PDAL classification filters and raster-writer settings on current swissSURFACE3D tiles.
