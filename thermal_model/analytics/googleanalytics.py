import requests
from datetime import datetime, UTC
import streamlit as st
import uuid

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfS1GxRyyXllykkruGhrREtvykGjG9LWFV_7sChZJ_I0HdEhQ/formResponse"
COUNT_ID = "entry.1147522663"
ENTRY_TIMESTAMP = "entry.731613908"
SESSION_ID = "entry.1008570580"

def record_visit():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())

    try:
        response = requests.post(
            FORM_URL,
            data={COUNT_ID: 1,
                ENTRY_TIMESTAMP: datetime.now(UTC).strftime("%Y-%m-%d"),
                SESSION_ID: st.session_state["session_id"]},
            timeout=5,
        )
        print(f"URL used: {response.url}")
        print("Visit recorded successfully.")
    except Exception:
        print("Failed to record visit to Google Form for analytics.")
        pass  # never crash the app over analytics

"""

https://docs.google.com/forms/d/e/1FAIpQLSfS1GxRyyXllykkruGhrREtvykGjG9LWFV_7sChZJ_I0HdEhQ/viewform?usp=pp_url&entry.1147522663=1&entry.731613908=2&entry.1008570580=fifteen
"""