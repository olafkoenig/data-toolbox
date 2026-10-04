# CLI

`dj-new` copies `templates/project` to a new directory. `dj-add` copies one maintained helper into the nearest project's `src/` directory. Both commands have no third-party CLI dependencies, refuse overwrites and never run `git init`.

```text
dj-new PROJECT_NAME [--parent DIRECTORY]
dj-add --list
dj-add HELPER [--project DIRECTORY]
```

Keep the `cli` directory with the repository: the command resolves the project template relative to its own file location.

On macOS or Linux, install it once from the repository root:

```bash
mkdir -p "$HOME/.local/bin"
ln -s "$PWD/cli/dj-new" "$HOME/.local/bin/dj-new"
ln -s "$PWD/cli/dj-add" "$HOME/.local/bin/dj-add"
command -v dj-new dj-add
```

After that, both commands work from any directory. `dj-add` walks up to the nearest directory containing `_quarto.yml` and `scripts/`, so it also works from inside `scripts/`. If `command -v` prints nothing, add `export PATH="$HOME/.local/bin:$PATH"` to `~/.zshrc` and start a new terminal.
