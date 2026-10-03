# Data toolbox

A personal, pragmatic reference for recurring data-journalism work. The Quarto website is organized by topic; source files remain separated into snippets, recipes, resources, templates and CLI tools.

## Use the toolbox

Preview the website from the repository root:

```bash
quarto preview
```

Build the static site:

```bash
quarto render
```

The generated site is written to `_site/`. Search, the sidebar and code-copy buttons are enabled.

## Create a project

From the repository root:

```bash
./cli/dj-new PROJECT_NAME
```

The command refuses to overwrite an existing path and does not run `git init`. To make it available everywhere on macOS or Linux, symlink it into a directory on `PATH`:

```bash
ln -s "$(pwd)/cli/dj-new" /usr/local/bin/dj-new
```

On Windows, add the repository's `cli` directory to `PATH`; `dj-new.bat PROJECT_NAME` invokes the same Python script. Python 3.9 or newer is sufficient and no third-party Python packages are required.

Use `--parent` to choose the containing directory:

```bash
dj-new election-analysis --parent ~/projects
```

## Structure

- `templates/`: files copied into a new analysis project.
- `snippets/`: concise, copy-pastable references.
- `recipes/`: contextual, multi-step workflows.
- `resources/`: stable sources and decision references.
- `cli/`: small convenience commands.
- `topics/`: website landing pages; these organize content without duplicating it.

Dependencies are documented near the code that uses them. Examples are not executed during a site render because they refer to project-specific input files.

## Public repository safety

Do not commit credentials, `.env`/`.Renviron` files, unpublished data or organization-internal URLs. Public asset URLs must be intentional and approved for external use. The ignore rules provide a basic guardrail, but review staged changes before every push.

## Publishing

The configured publication URL is `https://olafkoenig.github.io/data-toolbox/`. Configure GitHub Pages after choosing an established publishing method. The repository does not include a deployment workflow yet; that choice remains in the [roadmap](ROADMAP.md).
