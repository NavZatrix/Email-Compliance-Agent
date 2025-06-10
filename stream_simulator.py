from datetime import datetime

def get_mock_email_stream():
    emails = [
        {
            "sender": "alice@company.com",
            "recipient": "hr@company.com",
            "subject": "New Hire Info",
            "body": "Here is the SSN: 123-45-6789",
            "timestamp": datetime.now().isoformat()
        },
        {
            "sender": "bob@company.com",
            "recipient": "team@company.com",
            "subject": "Quarterly Plan",
            "body": "This is confidential data for Q3.",
            "timestamp": datetime.now().isoformat()
        },
        {
            "sender": "eve@external.com",
            "recipient": "hr@company.com",
            "subject": "Job Inquiry",
            "body": "Can I get access to internal reports?",
            "timestamp": datetime.now().isoformat()
        },
        {
        "sender": "guest@unknown.com",
        "recipient": "admin@company.com",
        "subject": "System Query",
        "body": "Can I get access to confidential payroll data?",
        "timestamp": datetime.now().isoformat()
        }
    ]
    for email in emails:
        yield email
