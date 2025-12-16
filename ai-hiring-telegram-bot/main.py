import requests
from config import BOT_TOKEN, CHANNEL_USERNAME
from fetch_data import fetch_jobs, fetch_internships, fetch_hackathons
from formatter import format_message
from posted_store import load_posted, save_posted, is_duplicate, mark_posted


def send_message(text):
    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    requests.post(url, data={
        "chat_id": CHANNEL_USERNAME,
        "text": text
    })


posted_set = load_posted()

def post_list(items):
    global posted_set

    for item in items:
        unique_id = f"{item['type']}_{item['role']}_{item['company']}"

        if is_duplicate(unique_id, posted_set):
            continue

        message = format_message(
            item["type"],
            item["role"],
            item["company"],
            item["location"],
            item["pay"],
            item["desc"]
        )

        send_message(message)
        mark_posted(unique_id, posted_set)

    save_posted(posted_set)


print("🚀 Posting Internships...")
post_list(fetch_internships())

print("🚀 Posting Jobs...")
post_list(fetch_jobs())

print("🚀 Posting Hackathons...")
post_list(fetch_hackathons())

print("✅ All posts done")
