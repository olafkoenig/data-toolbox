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

After installation, run the command from any directory:

```bash
dj-new PROJECT_NAME
```

The command refuses to overwrite an existing path and does not run `git init`.

On macOS or Linux, install both small commands once from the repository root:

```bash
mkdir -p "$HOME/.local/bin"
ln -s "$PWD/cli/dj-new" "$HOME/.local/bin/dj-new"
ln -s "$PWD/cli/dj-add" "$HOME/.local/bin/dj-add"
command -v dj-new dj-add
```

The last command should print two paths in `.local/bin`. If it prints nothing, add `export PATH="$HOME/.local/bin:$PATH"` to `~/.zshrc` and start a new terminal. Keep the repository in place: the symlinks deliberately use its template, helper catalog and CLI updates.

Without installation, `./cli/dj-new PROJECT_NAME` works only when the current directory is the repository root.

On Windows, add the repository's `cli` directory to `PATH`; the `dj-new.bat` and `dj-add.bat` launchers invoke the same Python scripts. Python 3.9 or newer is sufficient and no third-party CLI packages are required.

Use `--parent` to choose the containing directory:

```bash
dj-new election-analysis --parent ~/projects
```

Add a maintained helper to the nearest project without coupling that project to future toolbox changes:

```bash
dj-add --list
dj-add map-topology
```

`dj-add` copies the selected file into `src/`, prints the import statement and refuses to overwrite existing project code. Each associated website page documents the command, dependencies, import and minimal usage.

## Structure

- `templates/`: files copied into a new analysis project.
- `snippets/`: concise, copy-pastable references.
- `recipes/`: contextual, multi-step workflows.
- `resources/`: stable sources and decision references.
- `cli/`: small convenience commands.
- `helpers/`: maintained R and Python files copied into projects by `dj-add`.
- `topics/`: website landing pages; these organize content without duplicating it.

Dependencies are documented near the code that uses them. Examples are not executed during a site render because they refer to project-specific input files.

## Public repository safety

Do not commit credentials, `.env`/`.Renviron` files, unpublished data or organization-internal URLs. Public asset URLs must be intentional and approved for external use. The ignore rules provide a basic guardrail, but review staged changes before every push.

## Publishing

The website is published at `https://olafkoenig.github.io/data-toolbox/`. A GitHub Actions workflow renders and deploys the site after every push to `main`; it can also be run manually from the Actions tab.
