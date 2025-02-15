import sqlite3
from gmail.models import Email

class Database:
    def __init__(self, src = "emails.db") -> None:
        self.conn = sqlite3.connect(src)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS emails (
                id VARCHAR(255) PRIMARY KEY,
                timestamp INT,
                sender VARCHAR(255),
                receiver VARCHAR(255),
                subject VARCHAR(255),
                body TEXT
            )
        """)

        self.conn.commit()

    def save_email(self, email: Email):

        self.cursor.execute("INSERT OR IGNORE INTO emails (id, timestamp, sender, receiver, subject, body) VALUES (?, ?, ?, ?, ?, ?)", 
                    (email.id, email.timestamp, email.sender, email.receiver, email.subject, email.body))

        self.conn.commit()

    def save_email_multiple(self, emails: list[Email]):
        print("saving emails.")
        for email in emails:
            self.save_email(email)
        print("savied all emails.")

    def get_emails(self, limit) -> list[Email]:
        self.cursor.execute(f"SELECT * FROM emails ORDER BY timestamp DESC LIMIT {limit}")
        rows = self.cursor.fetchall()
        print("fetched ", len(rows), " emails.")
        return [Email(*row) for row in rows]

    def __del__(self):
        self.conn.close()