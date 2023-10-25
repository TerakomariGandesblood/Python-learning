fmt:
    rye run ruff format .
    prettier --write .
    taplo fmt *toml
    just --fmt --unstable

update:
    rye sync --update-all

check:
    pre-commit run --all-files
    rye run pyright .
    rye run ruff check .
    autocorrect --lint
