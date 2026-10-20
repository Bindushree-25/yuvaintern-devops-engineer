# Week 1 — DevOps Hello World

## Purpose
A minimal Python HTTP service for the YuvaIntern DevOps Engineer Fresher Fundamentals and Setup task.

## Requirements
- Python 3.10 or newer
- Git
- A terminal and code editor

## Run locally
From this folder, run:

```bash
python -m app.main
```

Open `http://127.0.0.1:8080/` and `http://127.0.0.1:8080/health`.

Expected examples:
- `/` returns HTTP 200 and `{"message": "Hello, DevOps!", "status": "ok"}`
- `/health` returns HTTP 200 and `{"status": "ok"}`
- an unknown route returns HTTP 404

These are expected responses. Run the service yourself and record the actual output in your report.

## Git starter workflow
```bash
git init
git status
git add README.md app/main.py .gitignore
git commit -m "feat: add DevOps hello-world service"
```

Create a GitHub repository, then follow GitHub's instructions to add the remote and push the code. Use your own repository URL in the YuvaIntern submission form. Never commit passwords, API keys, tokens, or private configuration.
