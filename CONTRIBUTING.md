# Contributing to neuroglow

## Dev setup

You need [uv](https://docs.astral.sh/uv/getting-started/installation/) and Node 20+.

```bash
git clone https://github.com/<your-fork>/neuroglow.git
cd neuroglow
uv sync
uv run pre-commit install
```

## Running tests

```bash
uv run pytest
```

## Linting

```bash
uv run ruff check .
uv run ruff format --check .
```

Auto-fix:

```bash
uv run ruff check --fix .
uv run ruff format .
```

## Front end

```bash
cd frontend
npm install
npm run build
```

The built assets go to `frontend/dist/` and are later copied to `src/neuroglow/static/` for bundling into the wheel. That copy step is not wired up yet — this is Milestone 0.

## Submitting changes

1. Create a branch from `main`.
2. Make your changes and ensure `uv run pytest` and `uv run ruff check .` pass.
3. Open a pull request with a clear description.
