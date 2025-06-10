#  Email Compliance Classifier Agent

##  System Use Case and Rationale

This agent simulates intelligent classification of email messages for organizations, helping enforce content compliance policies automatically. It ensures that flagged content is only accessible to users with proper privileges.

##  Governance Rules Used

- PII (like SSNs) must only be accessible by HR.
- Confidential content can be viewed by HR and Engineering.
- External or Guest roles cannot access flagged content.

##  Architectural Tradeoffs and Constraints

| Area             | Design Choice                        | Justification |
|------------------|--------------------------------------|---------------|
| Storage Types    | SQLite (SQL) + JSON (NoSQL-style)    | SQL for structured data, JSON for flexible logging |
| Data Flow        | Streaming with 1s delay              | Mimics real-world message arrival |
| Governance Model | PBAC: Role-based access simulation   | Enforces identity-driven decisions |
| CAP Tradeoff     | Availability + Partition Tolerance   | SQLite is resilient; logs are async |

##  How to Run

1. Extract the folder.
2. Open terminal in the project folder.
3. Run:

```bash
python main.py
```

4. Check `decision_logs.json` and `approved.db`.

##  Roles

- HR: Full Access
- Engineering: Confidential Only
- External: No Access to Sensitive Data

##  Enhancements

- Add ABAC context control
- Add OpenAI moderation
- Visual dashboard with Flask or Streamlit
