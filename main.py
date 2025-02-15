from gmail import fetch_emails, creds
from database import db
from checker import read_rules, Processor

limit = 5
emails = fetch_emails(limit)
db.save_email_multiple(emails)
emails = db.get_emails(limit)
rule_processor = Processor("rules.json")
matches = rule_processor.process_emails(emails, "rule-2")