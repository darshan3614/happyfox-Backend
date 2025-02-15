from dataclasses import dataclass
import time
import datetime

@dataclass
class Email:
    id: str
    timestamp: int
    sender: str
    receiver: str
    subject: str
    body: str

    def __getitem__(self, key: str):
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(f"'{key}' not found in Email")

    def check_text(self, field, predicate, value):
        if predicate == "contains":
            return value in field
        elif predicate == "equals":
            return value == field
        elif predicate == "does_not_contain":
            return value not in field
        elif predicate == "does_not_equal":
            return value != field
        else:
            raise Exception("Invalid predicate")

    def check_num(self, field, predicate, value):
        if predicate == 'less_than':
            return value * 60 * 60 * 24 > time.time() - field
        elif predicate == 'greater_than':
            return value * 60 * 60 * 24 < time.time() - field
        else:
            raise Exception("Invalid predicate")

    def check_field(self, field, predicate, value):
        if(field == 'timestamp'):
            if(type(value) == str):
                raise TypeError("Expecting an integer for numeric comparision.")
            if(not (predicate.endswith("months") or predicate.endswith("days"))):
                raise ValueError("Expected day/month format spcifier.")
            predicate, n = predicate.split(":")

            #convert to days if months
            if(n == 'months'):
                value * 31
            return self.check_num(self[field], predicate, value)
        else:
            return self.check_text(self[field].lower(), predicate, value.lower())