import requests
from datetime import datetime, UTC
import streamlit as st

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfS1GxRyyXllykkruGhrREtvykGjG9LWFV_7sChZJ_I0HdEhQ/formResponse"
COUNT_ID = "entry.1147522663"
ENTRY_TIMESTAMP = "entry.731613908"

def record_visit():
    print("Recording visit to Google Form for analytics...")
    # try:
    response = requests.post(
        FORM_URL,
        data={COUNT_ID: 1,
              ENTRY_TIMESTAMP: datetime.now(UTC).strftime("%Y-%m-%d")},
        timeout=5,
    )
    print(f"Status: {response.status_code}")
    print(f"URL used: {response.url}")
    print("Visit recorded successfully.")
    # except Exception:
    #     print("Failed to record visit to Google Form for analytics.")
    #     pass  # never crash the app over analytics

"""

https://docs.google.com/forms/d/e/1FAIpQLSfS1GxRyyXllykkruGhrREtvykGjG9LWFV_7sChZJ_I0HdEhQ/viewform?
usp=pp_url&
entry.1147522663=2
&
entry.731613908=2026-05-03

"""