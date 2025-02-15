import json

def read_rules(file_path) -> dict:
    with open(file_path, "r") as file:
        rules = json.load(file)
    return rules