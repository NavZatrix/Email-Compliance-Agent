import time
import json
from access_control import get_user_role, has_access
from policy_rules import apply_policy_rules
from stream_simulator import get_mock_email_stream
import sqlite3

# Setup SQLite DB for approved emails
conn = sqlite3.connect("approved.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS approved_emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT, recipient TEXT, subject TEXT, body TEXT, timestamp TEXT
)''')
conn.commit()

def log_decision(log):
    with open("decision_logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")

print("\n[Agent Started] Monitoring incoming emails...\n")

for email in get_mock_email_stream():
    user_role = get_user_role(email['sender'])
    policy_result = apply_policy_rules(email)

    decision_log = {
        "email_subject": email['subject'],
        "sender": email['sender'],
        "role": user_role,
        "timestamp": email['timestamp'],
        "policy_result": policy_result
    }

    if policy_result['flagged']:
        if has_access(user_role, policy_result['reason']):
            cursor.execute("INSERT INTO approved_emails (sender, recipient, subject, body, timestamp) VALUES (?, ?, ?, ?, ?)",
                           (email['sender'], email['recipient'], email['subject'], email['body'], email['timestamp']))
            conn.commit()
            decision_log['action'] = 'approved with elevated access'
        else:
            decision_log['action'] = 'flagged and not stored'
    else:
        cursor.execute("INSERT INTO approved_emails (sender, recipient, subject, body, timestamp) VALUES (?, ?, ?, ?, ?)",
                       (email['sender'], email['recipient'], email['subject'], email['body'], email['timestamp']))
        conn.commit()
        decision_log['action'] = 'approved'

    log_decision(decision_log)
    print(f"Processed: {email['subject']} -> {decision_log['action']}")
    time.sleep(1)

conn.close()
