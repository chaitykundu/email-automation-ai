import email
from email.header import decode_header


def decode_mime_words(s):

    decoded_words = decode_header(s)
    decoded_string = ""

    for word, encoding in decoded_words:

        if isinstance(word, bytes):

            decoded_string += word.decode(
                encoding or "utf-8",
                errors="ignore"
            )

        else:
            decoded_string += word

    return decoded_string


def extract_email_body(message):

    body = ""

    if message.is_multipart():

        for part in message.walk():

            content_type = part.get_content_type()
            content_disposition = str(
                part.get("Content-Disposition")
            )
            print(f"Processing part with content type: {content_type}")

            if (
                content_type == "text/plain"
                and "attachment" not in content_disposition
            ):

                payload = part.get_payload(decode=True)

                if payload:
                    body += payload.decode(
                        errors="ignore"
                    )
                    print(f"Extracted text/plain part: {body[:500]}")

    else:

        payload = message.get_payload(decode=True)

        if payload:
            body = payload.decode(errors="ignore")
            print(f"Extracted body for non-multipart email: {body[:500]}")

    return body