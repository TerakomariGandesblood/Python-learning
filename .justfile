fmt:
    black .
    prettier --write .
    just --fmt --unstable

check:
    pre-commit run --all-files
    mypy .
    ruff check .
    autocorrect --lint
