# Download and read a dated G1 or K4 administrative layer.
# Source: data-toolbox helper `swiss-geometries-r`.

get_swiss_geometries <- function(product = c("g1", "k4"),
                                 date,
                                 level = c(
                                   "communes",
                                   "districts",
                                   "cantons",
                                   "country",
                                   "lakes"
                                 ),
                                 raw_dir) {
  product <- match.arg(product)
  level <- match.arg(level)

  if (missing(date) || length(date) != 1 || is.na(date)) {
    stop("`date` must be one value formatted as YYYY-MM-DD")
  }
  parsed_date <- suppressWarnings(as.Date(date, format = "%Y-%m-%d"))
  if (is.na(parsed_date) || format(parsed_date, "%Y-%m-%d") != date) {
    stop("`date` must be formatted as YYYY-MM-DD")
  }
  if (missing(raw_dir) || length(raw_dir) != 1) {
    stop("`raw_dir` must be one project directory")
  }

  collection_id <- paste0(
    "ch.bfs.historisierte-administrative_grenzen_",
    product
  )
  item_id <- paste0(
    "historisierte-administrative_grenzen_",
    product,
    "_",
    date
  )
  item_url <- paste0(
    "https://data.geo.admin.ch/api/stac/v1/collections/",
    collection_id,
    "/items/",
    item_id
  )

  response <- httr2::request(item_url) |>
    httr2::req_perform()
  httr2::resp_check_status(response)
  item <- httr2::resp_body_json(response, simplifyVector = FALSE)

  gpkg_assets <- Filter(
    function(asset) identical(
      asset$type,
      "application/geopackage+sqlite3"
    ),
    item$assets
  )
  if (length(gpkg_assets) != 1) {
    stop("Expected one GPKG asset; found ", length(gpkg_assets))
  }

  dir.create(raw_dir, recursive = TRUE, showWarnings = FALSE)
  destination <- file.path(raw_dir, basename(gpkg_assets[[1]]$href))

  if (!file.exists(destination)) {
    httr2::request(gpkg_assets[[1]]$href) |>
      httr2::req_perform(path = destination)
  }

  layer_roots <- c(
    communes = "Communes",
    districts = "Districts",
    cantons = "Cantons",
    country = "Country",
    lakes = "Lacs"
  )
  layer_pattern <- paste0(
    "^",
    layer_roots[[level]],
    "_",
    toupper(product),
    "_",
    gsub("-", "", date),
    "$"
  )
  layer <- grep(
    layer_pattern,
    sf::st_layers(destination)$name,
    value = TRUE
  )
  if (length(layer) != 1) {
    stop("Expected one layer for `", level, "`; found ", length(layer))
  }

  sf::st_read(destination, layer = layer, quiet = TRUE)
}
