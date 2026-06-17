# email-automation-ai
# AI Email Automation System

## Overview

This project is a FastAPI-based email automation system that connects to a Gmail inbox, fetches unread emails, and extracts important email information such as sender, subject, and email body.

The goal is to build a foundation for future AI-powered email processing and automation workflows.

## Features Implemented

* FastAPI backend setup
* Environment variable management using `.env`
* Gmail IMAP integration
* Secure authentication using Gmail App Password
* Fetch unread emails from inbox
* Extract email subject
* Extract sender information
* Decode MIME encoded subjects
* Extract plain text email body
* Swagger API documentation

## Project Structure

```text
email-automation-ai/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   │           ├── health.py
│   │           └── email.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── email/
│   │   ├── imap_client.py
│   │   └── parser.py
│   │
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

## How It Works

1. The FastAPI server starts and loads configuration from the `.env` file.
2. The application connects to Gmail using IMAP and an App Password.
3. It searches for unread emails in the inbox.
4. For each email, the system extracts:

   * Email UID
   * Subject
   * Sender
   * Email Body
5. The extracted information is returned through the API endpoint.

## API Endpoints

### Health Check

```http
GET /api/v1/health
```

### Fetch Emails

```http
GET /api/v1/fetch-emails
```

## Technologies Used

* FastAPI
* Uvicorn
* IMAPClient
* Python Email Library
* Pydantic Settings
* Python Dotenv

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```
