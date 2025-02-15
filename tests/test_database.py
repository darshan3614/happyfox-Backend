import unittest
from database import Database
from gmail import Email

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def test_save_email(self):

        # check if mail was saved
        self.db.save_email(Email("3", 8347346, "sender@gmail.com", "receiver@gmail.com", "Gmail- Test Subject.", "This is a mail body."))
        new_len = len(self.db.get_emails(10))
        self.assertEqual(new_len, 1)

    def test_fetch_email(self):

        #check if saved and retrieved mail are same or not
        email_orig = Email("3", 8347346, "sender@gmail.com", "receiver@gmail.com", "Gmail- Test Subject.", "This is a mail body.")
        self.db.save_email(email_orig)
        email_fetch = self.db.get_emails(10)[0]
        self.assertEqual(email_fetch.id, email_orig.id)
        self.assertEqual(email_fetch.timestamp, email_orig.timestamp)
        self.assertEqual(email_fetch.sender, email_orig.sender)
        self.assertEqual(email_fetch.receiver, email_orig.receiver)
        self.assertEqual(email_fetch.body, email_orig.body)

    def tearDown(self):
        self.db.conn.close()