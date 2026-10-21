"""
Angelou Fiel — AI Automation Portfolio (FastAPI)
Run locally:  uvicorn main:app --reload
"""
import os
import json
import smtplib
import datetime
from email.message import EmailMessage
from pathlib import Path

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI(title="Angelou Fiel — AI Automation Portfolio")

BASE = Path(__file__).parent
LEADS = BASE / "leads.jsonl"


def notify_email(record: dict) -> None:
    """Email you when a lead comes in. Off unless SMTP env vars are set.
    For Gmail: SMTP_HOST=smtp.gmail.com, SMTP_USER=you@gmail.com,
    SMTP_PASS=<a Gmail App Password>, NOTIFY_TO=you@gmail.com
    """
    host = os.getenv("SMTP_HOST")
    user = os.getenv("SMTP_USER")
    pw = os.getenv("SMTP_PASS")
    to = os.getenv("NOTIFY_TO", user or "")
    if not (host and user and pw and to):
        return  # email notifications not configured -> just saved to file

    msg = EmailMessage()
    msg["Subject"] = f"New portfolio lead: {record['name']}"
    msg["From"] = user
    msg["To"] = to
    msg.set_content(
        f"Name: {record['name']}\n"
        f"Contact: {record['email']}\n\n"
        f"{record['message']}\n\n"
        f"Received: {record['at']}"
    )
    try:
        with smtplib.SMTP(host, int(os.getenv("SMTP_PORT", "587"))) as s:
            s.starttls()
            s.login(user, pw)
            s.send_message(msg)
    except Exception as e:  # never let email break the response
        print("Email notify failed:", e)


@app.get("/")
def home():
    """Serve the cinematic portfolio page."""
    return FileResponse(BASE / "index.html")


@app.post("/api/contact")
def contact(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    """Receive a contact message and store it as a lead."""
    record = {
        "name": name.strip(),
        "email": email.strip(),
        "message": message.strip(),
        "at": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    with LEADS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    notify_email(record)
    return JSONResponse({"ok": True, "message": "Thanks! I'll get back to you soon."})


@app.get("/health")
def health():
    return {"status": "ok"}
