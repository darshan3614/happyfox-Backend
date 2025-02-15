import base64

def get_email_body(payload):
    body = ""
    
    if "parts" in payload:  
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":  
                body = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
                break
            elif part["mimeType"] == "text/html":  
                body = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
    else:  
        body = base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8")

    return body.strip() if body else "No Body"