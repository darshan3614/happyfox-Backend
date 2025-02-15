import unittest
from gmail import fetch_emails
from checker import Processor

class TestChecker(unittest.TestCase):

    def setUp(self):
        self.processor = Processor("tests/test_rule.json")

    def test_email_checker(self):
        emails = fetch_emails(1)

        # passing str for time based filter
        self.assertRaises(TypeError, self.processor.process_emails, emails, "rule-error-type")

        # passing a rule that was not present
        self.assertRaises(Exception, self.processor.process_emails, emails, "rule-error-not-found")

        matches = self.processor.process_emails(emails, "rule-success")
        self.assertEqual(len(matches), 1)

        
