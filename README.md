# neuroglow

A live training visualizer for PyTorch. Add `neuroglow.watch(model)` to your training loop and watch your model learn in real time in a browser tab.

> **Status: early development** — not yet usable. This is Milestone 0 (project skeleton only).

## Dev setup

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/) and Node 20+.

```bash
git clone https://github.com/<your-username>/neuroglow.git
cd neuroglow
uv sync
uv run pre-commit install
```

Run tests:

```bash
uv run pytest
```
