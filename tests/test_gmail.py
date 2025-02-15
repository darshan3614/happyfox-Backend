import unittest
from gmail import Email, authenticate, fetch_emails
from googleapiclient.discovery import build

class TestGmail(unittest.TestCase):

    def test_fetch_email(self):
        emails = fetch_emails(1)

        # check if mail was fetched or not
        self.assertIsNotNone(emails)

        # check if mail attributes are mapped to Email model or not
        self.assertIsInstance(emails[0], Email)