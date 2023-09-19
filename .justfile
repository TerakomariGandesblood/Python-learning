fmt:
    rye run black .
    prettier --write .
    taplo fmt *toml
    just --fmt --unstable

update:
    rye sync --update-all

check:
    pre-commit run --all-files
    rye run mypy .
    rye run ruff .
    autocorrect --lint
