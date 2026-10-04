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

On macOS or Linux, install it once from the repository root:

```bash
mkdir -p "$HOME/.local/bin"
ln -s "$PWD/cli/dj-new" "$HOME/.local/bin/dj-new"
command -v dj-new
```

The last command should print a path ending in `.local/bin/dj-new`. If it prints nothing, add `export PATH="$HOME/.local/bin:$PATH"` to `~/.zshrc` and start a new terminal. Keep the repository in place: the symlink deliberately uses its template and CLI updates.

Without installation, `./cli/dj-new PROJECT_NAME` works only when the current directory is the repository root.

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

The website is published at `https://olafkoenig.github.io/data-toolbox/`. A GitHub Actions workflow renders and deploys the site after every push to `main`; it can also be run manually from the Actions tab.
