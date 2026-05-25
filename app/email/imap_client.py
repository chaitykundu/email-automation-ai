from imapclient import IMAPClient
from app.core.config import settings


def connect_to_email():

    server = IMAPClient(
        settings.IMAP_SERVER,
        port=settings.IMAP_PORT,
        ssl=True
    )

    server.login(
        settings.EMAIL_ADDRESS,
        settings.EMAIL_PASSWORD
    )

    return server