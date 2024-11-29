update:
    uv lock --upgrade
    uv sync --all-extras --dev

fmt:
    uv run --frozen ruff format
    prettier --write .
    taplo fmt *toml
    just --fmt --unstable

check:
    pre-commit run --all-files
    uv run --frozen ruff check
    uv run --frozen pyright
