from .auth import service
from .helper import get_email_body
from .models import Email
from flanker.addresslib import address

def fetch_emails(max_results) -> list[Email]:

    results = service.users().messages().list(userId="me", maxResults = max_results).execute()
    messages = results.get("messages", [])

    emails = []

    for msg in messages:
        msg_id = msg["id"]
        message = service.users().messages().get(userId="me", id=msg_id, format="full").execute()

        headers = message["payload"]["headers"]
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown Sender")
        receiver = next((h["value"] for h in headers if h["name"] == "To"), "Unknown Sender")
        
        timestamp = int(message["internalDate"]) // 1000
        sender = address.parse(sender).address
        receiver = address.parse(receiver).address
        body = get_email_body(message["payload"])

        emails.append(Email(msg_id, timestamp, sender, receiver, subject, body))

    print(len(emails), " emails found.")
    return emails
