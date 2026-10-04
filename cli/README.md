# CLI

`dj-new` copies `templates/project` to a new directory. It has no third-party dependencies, does not overwrite existing paths and does not run `git init`.

```text
dj-new PROJECT_NAME [--parent DIRECTORY]
```

Keep the `cli` directory with the repository: the command resolves the project template relative to its own file location.

On macOS or Linux, install it once from the repository root:

```bash
mkdir -p "$HOME/.local/bin"
ln -s "$PWD/cli/dj-new" "$HOME/.local/bin/dj-new"
command -v dj-new
```

After that, `dj-new PROJECT_NAME` works from any directory. If `command -v` prints nothing, add `export PATH="$HOME/.local/bin:$PATH"` to `~/.zshrc` and start a new terminal.
