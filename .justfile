fmt:
    rye fmt
    prettier --write .
    taplo fmt *toml
    just --fmt --unstable

update:
    rye sync --update-all

check:
    pre-commit run --all-files
    rye run pyright .
    rye lint
    autocorrect --lint
