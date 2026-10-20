# Week 3 — Practical Implementation Project

This folder contains a small Python HTTP service and automated unit tests. It is designed to demonstrate practical implementation, separation of concerns, repeatable tests, and a basic local development workflow.

## Requirements
- Python 3.9 or later
- No third-party packages required

## Run automated tests
From this folder (`week3-practical-implementation`):

```bash
python -m unittest discover -s tests -v
```

The suite contains five unit tests covering the root, health, version, unknown-route, and JSON-serialization behavior. The expected result is five passing tests; record the actual result only after running the command.

## Run the service
From this folder:

```bash
python -m app.main
```

Open `http://127.0.0.1:8000/`, `/health`, or `/version`. Press Ctrl+C to stop the service. If port 8000 is already in use, stop the conflicting process or consistently change the port in `app/main.py`.

## Structure
- `app/service.py` — route decisions and JSON serialization
- `app/main.py` — HTTP server adapter
- `tests/test_service.py` — automated unit tests

## Scope and limitations
This is a learning example using Python's built-in HTTP server. It is not production hardened and does not include authentication, TLS, containerization, external monitoring, or a CI pipeline. Tests cover the route-decision function and serialization, not a full live-server integration test.

## Existing GitHub repository
Add this entire `week3-practical-implementation` folder to the existing `yuvaintern-devops-engineer` repository. Keep the Week 1 and Week 2 files intact. Suggested commit message: `Add Week 3 practical implementation and unit tests`.
