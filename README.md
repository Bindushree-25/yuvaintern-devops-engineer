# Week 4 — Testing and Quality Assurance

A small Python service used to demonstrate positive tests, negative tests, boundary/contract validation, test documentation, and repeatable QA.

## Requirements
Python 3.9+; no third-party packages required.

## Run tests
From this folder:

```bash
python -m unittest discover -s tests -v
```

Eight tests are included. Run them and record the actual output; the count is an expected suite size, not proof that tests passed in your environment.

## Run service
```bash
python -m app.main
```
Then visit `http://127.0.0.1:8000/`, `/health`, and `/version`. Stop with Ctrl+C.

## Structure
- `app/service.py` — route logic and basic response-contract validation
- `app/main.py` — HTTP server adapter
- `tests/test_service.py` — automated tests
- `tests/TEST_CASES.md` — test cases and QA plan
- `TEST_EVIDENCE.md` — record actual results and any defect/fix cycle

## Limitations
This is a learning project, not production QA. It does not include load testing, security testing, a live-server integration suite, external monitoring, or CI automation. The contract validator is intentionally small and is not a complete HTTP schema validator.

Add this folder to the existing `yuvaintern-devops-engineer` GitHub repository without replacing earlier weeks.
