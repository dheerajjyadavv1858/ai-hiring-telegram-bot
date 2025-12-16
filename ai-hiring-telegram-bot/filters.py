from datetime import datetime, timedelta

def is_last_24_hours(post_time):
    return post_time >= datetime.now() - timedelta(hours=24)

def is_engineering(text):
    keywords = [
        "engineering", "engineer", "developer",
        "software", "computer science", "btech", "tech"
    ]
    text = text.lower()
    return any(k in text for k in keywords)

def valid_internship(stipend):
    return 5000 <= stipend <= 30000

def valid_job(salary):
    return salary >= 35000
