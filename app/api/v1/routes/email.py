from fastapi import APIRouter
from app.email.imap_client import connect_to_email

router = APIRouter()


@router.get("/fetch-emails")
def fetch_emails():

    server = connect_to_email()

    server.select_folder("INBOX")

    messages = server.search(["UNSEEN"])

    email_list = []

    for uid in messages:

        message_data = server.fetch(
            [uid],
            ["ENVELOPE"]
        )

        envelope = message_data[uid][b"ENVELOPE"]

        subject = envelope.subject.decode()

        sender = envelope.from_[0].mailbox.decode()

        email_list.append({
            "uid": uid,
            "subject": subject,
            "sender": sender
        })

    server.logout()

    return {
        "emails": email_list
    }