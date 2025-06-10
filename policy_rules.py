import re

def apply_policy_rules(email):
    body = email['body']
    if re.search(r"\d{3}-\d{2}-\d{4}", body):
        return {"flagged": True, "reason": "PII"}
    elif "confidential" in body.lower():
        return {"flagged": True, "reason": "Confidential"}
    return {"flagged": False, "reason": "None"}
