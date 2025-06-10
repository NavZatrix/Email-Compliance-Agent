user_roles = {
    "alice@company.com": "HR",
    "bob@company.com": "Engineering",
    "eve@external.com": "External"
}

access_matrix = {
    "PII": ["HR"],
    "Confidential": ["HR", "Engineering"]
}

def get_user_role(email):
    return user_roles.get(email, "Guest")

def has_access(role, content_type):
    return role in access_matrix.get(content_type, [])
