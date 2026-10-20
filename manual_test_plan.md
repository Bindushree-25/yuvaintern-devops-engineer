# Week 2 Manual Test Plan

Start the service with `python app/main.py` from the project root, then check the following in a browser or terminal. These are planned checks; record the actual result from your own environment before claiming they passed.

| ID | Request | Expected status | Expected behavior |
|---|---|---:|---|
| T1 | `GET /` | 200 | JSON includes `message` and `version` |
| T2 | `GET /health` | 200 | JSON includes `status: ok` and `version` |
| T3 | `GET /version` | 200 | JSON includes the version string |
| T4 | `GET /not-a-route` | 404 | JSON includes `error: not_found` |

Example terminal commands (run in a second terminal while the service is running):

```bash
curl -i http://127.0.0.1:8000/
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/version
curl -i http://127.0.0.1:8000/not-a-route
```

## Evidence log
- Date/time checked:
- Python version (`python --version`):
- Operating system:
- T1 actual status/result:
- T2 actual status/result:
- T3 actual status/result:
- T4 actual status/result:
- Git commit hash:
- Notes/issues:
