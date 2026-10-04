# Project title

One sentence describing the question this project answers.

## Structure

- `input/raw/`: original source data; never overwrite it with cleaned data.
- `input/processed/`: persistent cleaned or intermediate datasets.
- `output/`: final exports.
- `scripts/`: acquisition, cleaning and analysis documents.
- `src/`: project-specific functions reused in several documents.

## Reproduce

1. Record source links and acquisition dates in `scripts/01_get_data.qmd`.
2. Create reusable processed data with `scripts/02_clean_data.qmd`.
3. Start analysis in `scripts/03_analysis.qmd` and add descriptively named analyses as the work branches.

Document project-specific system dependencies and manual steps here.

## Toolbox helpers

From the project root or a directory below it:

```bash
dj-add --list
dj-add HELPER
```

The command copies the selected helper into `src/`, prints how to load it and refuses to overwrite an existing file. Keep project-specific choices in the QMD; keep only reused functions in `src/`.
