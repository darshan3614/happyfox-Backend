from gmail import Email
from .reader import read_rules
from actions import action_runner
class Processor:
    def __init__(self, rule_file = "rules.json") -> None:
        self.rules = read_rules(rule_file)

    def process_emails(self, emails: list[Email], rule_id):
        print("Procesing rule ", rule_id)
        rule = self.get_rules(rule_id)
        matches = self.match_mails(emails, rule)
        print(len(matches), " matches found.")
        self.take_action_multiple(matches, rule['actions'])
        return matches

    def get_rules(self, rule_id):
        if(rule_id not in self.rules):
            raise Exception("Rule not found.")
        return self.rules[rule_id]

    def match_mails(self, emails: list[Email], rule):

        matches = []
        for email in emails:
            match_matrix = []
            for condition in rule['conditions']:
                match_matrix.append(email.check_field(*condition.values()))
            
            if(rule['match'] == 'all' and all(match_matrix)):
                matches.append(email)

            if(rule['match'] == 'any' and any(match_matrix)):
                matches.append(email)
        return matches

    def take_action(self, emails: list[Email], action_id):
        if(action_id.startswith('move-to')):
            to = action_id.split(":")[-1]
            action_runner.move_mailbox(emails, to)
        elif(action_id == 'mark-read'):
            action_runner.mark_read(emails) 
    
    def take_action_multiple(self, emails: list[Email], actions: list[str]):
        for action in actions:
            self.take_action(emails, action)