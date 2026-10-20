# Week 4 Test Cases and QA Plan

These are test definitions and expected outcomes. Record actual results only after running the suite on your own machine.

| ID | Scenario | Expected result | Category |
|---|---|---|---|
| TC-01 | Request `/` | HTTP-style status 200 and expected message/version | Positive / functional |
| TC-02 | Request `/health` | Status 200 and `status: ok` | Positive / functional |
| TC-03 | Request `/version` | Status 200 and version `4.0.0` | Positive / functional |
| TC-04 | Request `/unknown` | Status 404 and `error: not_found` | Negative / error handling |
| TC-05 | Status is a string | Contract validator rejects it | Negative / input validation |
| TC-06 | Payload is a list | Contract validator rejects it | Negative / type validation |
| TC-07 | Successful payload is empty | Contract validator rejects it | Boundary / validation |
| TC-08 | 404 payload has wrong error | Contract validator rejects it | Negative / contract validation |

## Run
From this folder:

```bash
python -m unittest discover -s tests -v
```

Expected by design: eight tests. Actual pass/fail counts must be copied from the command output after execution.
