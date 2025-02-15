Backend Assignment

Overview
This project is a standalone Python script that integrates with the Gmail API to fetch emails, process them based on predefined rules, and perform actions on them. The project follows a modular structure and includes unit tests using `unittest`. Additionally, it utilizes `flanker`, a library forked by HappyFox, for email parsing.

Features
- Authenticate to Gmail API using OAuth.
- Fetch emails from the inbox without using IMAP.
- Store emails in a relational database (SQLite3).
- Process emails based on user-defined rules stored in a JSON file.
- Perform actions like marking emails as read/unread and moving messages.
- Unit testing implemented using `unittest`.

Project Structure
```
backend_assignment/
│-- actions/
│   ├── main.py
│   ├── __init__.py
│
│-- checker/
│   ├── processor.py
│   ├── reader.py
│   ├── __init__.py
│
│-- database/
│   ├── main.py
│   ├── __init__.py
│
│-- gmail/
│   ├── auth.py
│   ├── fetch_emails.py
│   ├── helper.py
│   ├── models.py
│   ├── __init__.py
│
│-- tests/
│   ├── test_checker.py
│   ├── test_database.py
│   ├── test_gmail.py
│   ├── test_rule.json
│
│-- README.md
│-- requirements.txt
│-- config.json
│-- main.py
```

Installation
Prerequisites
- Python 3.8+
- A Google Cloud project with Gmail API enabled
- SQLite3 

Setup
1. Clone the repository:
   ```
   git clone https://github.com/darshan3614/happyfox-Backend.git
   cd happyfox-Backend
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up Gmail API credentials:
   - Create a project in the [Google Developer Console](https://console.cloud.google.com/).
   - Enable the Gmail API.
   - Download the OAuth credentials JSON file and save it as `credentials.json` in the root directory.

5. Configure the database:
   - Modify `config.json` to set up database connection details.
   ```json
   {
       "database": {
           "type": "sqlite",
           "name": "emails.db"
       }
   }
   ```

Run the Main Script
```bash
python main.py
```

Running Tests
To execute unit tests:
```bash
python -m unittest discover tests
```

Configuration
Rules File (`test_rule.json`)
Rules are stored in JSON format. Example:
```json
{
    "rules": [
        {
        "field": "from",
        "predicate": "contains",
        "value": example@domain.com
        }
    ],
    "match": "any",
    "actions": [
      "mark-read"
    ]
}
```

Technologies Used
- **Python**: Core programming language.
- **Gmail API**: Fetching and processing emails.
- **Flanker**: Email parsing and validation.
- **Unittest**: Testing framework.
- **SQLite**: Relational database for email storage.

Author
- [Darshan D Madiwalar](https://github.com/darshan3614)


