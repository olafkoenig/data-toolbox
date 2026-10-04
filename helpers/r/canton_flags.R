# Create Datawrapper-compatible canton labels using an approved asset host.
# Source: data-toolbox helper `canton-flags-r`.

canton_with_flag <- function(canton, base_url) {
  canton <- as.character(canton)

  if (length(base_url) != 1 || is.na(base_url) || !nzchar(base_url)) {
    stop("`base_url` must be one non-empty URL")
  }
  if (anyNA(canton) || any(!grepl("^[A-Z]{2}$", canton))) {
    stop("`canton` must contain two-letter uppercase canton codes")
  }

  base_url <- sub("/+$", "", base_url)
  sprintf("![%s](%s/%s.svg) %s", canton, base_url, canton, canton)
}
