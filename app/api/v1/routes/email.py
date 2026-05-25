from fastapi import APIRouter

from app.email.imap_client import connect_to_email
from app.email.parser import (
    decode_mime_words,
    extract_email_body
)

import email

router = APIRouter()


@router.get("/fetch-emails")
def fetch_emails():

    server = connect_to_email()
    print("Selecting INBOX folder...")

    server.select_folder("INBOX")

    messages = server.search(["UNSEEN"])

    email_list = []

    for uid in messages:

        raw_message = server.fetch(
            [uid],
            ["RFC822"]
        )
        print(f"Fetched email UID: {uid}")

        raw_email = raw_message[uid][b"RFC822"]

        message = email.message_from_bytes(raw_email)

        subject = decode_mime_words(
            message["Subject"]
        )
        print(f"Decoded subject: {subject}")

        sender = message["From"]
        print(f"Email sender: {sender}")

        body = extract_email_body(message)
        print(f"Extracted body for UID {uid}: {body[:500]}")
        print(f"\nProcessing email UID: {uid}")

        email_data = {
            "uid": uid,
            "subject": subject,
            "sender": sender,
            "body": body[:500]
        }

        print(email_data)

        email_list.append(email_data)
        print(f"Email UID {uid} processed.\n")

    server.logout()

    return {
        "emails": email_list
    }