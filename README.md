# YuvaIntern DevOps — Week 2: Core Concepts and Skills

This small Python HTTP service is a practice artifact for learning application structure, HTTP routes/status codes, health checks, versioning, manual test planning, and a basic Git change workflow.

## Requirements
- Python 3.9+ (uses only the Python standard library)
- Git and a GitHub account for version control

## Run locally
From the project root:

```bash
python app/main.py
```

Then open `http://127.0.0.1:8000/`, or use `curl` from a second terminal. Stop the service with Ctrl+C.

## Routes
- `GET /` — welcome message and version
- `GET /health` — basic health response
- `GET /version` — version response
- Any other path — JSON 404 response

## Test plan
See [`tests/manual_test_plan.md`](tests/manual_test_plan.md). The table lists expected behavior; update the evidence log with actual results from your own machine. Do not report a check as passed until you have run it.

## Suggested Git workflow
1. Add these files to the existing `yuvaintern-devops-engineer` repository.
2. Review the changed files before committing.
3. Commit with a descriptive message such as `Add Week 2 DevOps core concepts service`.
4. Push/upload the changes to GitHub and confirm the files are visible.

This project is a learning example, not a production-ready service. It binds to localhost, uses the built-in HTTP server, and has no authentication, TLS, external monitoring, or automated CI pipeline.
