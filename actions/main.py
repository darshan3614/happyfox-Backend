from gmail import service, Email

class Actions:
    def __init__(self) -> None:
        pass

    def create_label(self, label_name: str):

         label_body = {
             "name": label_name,
             "messageListVisibility": "show",
             "labelListVisibility": "labelShow",
         }

         new_label = service.users().labels().create(userId="me", body=label_body).execute()
         print(f"Created label '{label_name}' with ID: {new_label['id']}")

         return new_label["id"]

    def mark_read(self, emails: list[Email]):
        for email in emails:
            self.modify_label(email, remove=["UNREAD"])
            print("marked", email.subject, "as read.")

    def move_mailbox(self, emails: list[Email], to):

        labels_response = service.users().labels().list(userId="me").execute()
        labels = {label["name"]: label["id"] for label in labels_response.get("labels", [])}

        if to not in labels:
            print(f"label '{to}' not found.")
            labels[to] = self.create_label(to)

        new_label_id = labels[to]

        for email in emails:
            self.modify_label(email, add=[new_label_id])
            print("moved", email.subject, "to", to)
    
    def modify_label(self, email: Email, add: list[str] = [], remove: list[str] = []):

        body = {}

        if(add):
            body["addLabelIds"] = add
        if(remove):
            body["removeLabelIds"] = remove

        service.users().messages().modify(
                userId="me",
                id=email.id,
                body=body
            ).execute()