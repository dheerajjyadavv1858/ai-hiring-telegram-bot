import requests
import feedparser
from datetime import datetime, timedelta

def is_last_24_hours(dt):
    return dt >= datetime.now() - timedelta(hours=24)

# -------- JOBS (Indeed RSS) --------
def fetch_jobs():
    feed = feedparser.parse(
        "https://www.indeed.com/rss?q=software+engineer&l=India"
    )

    jobs = []
    for entry in feed.entries:
        published = datetime(*entry.published_parsed[:6])
        if not is_last_24_hours(published):
            continue

        jobs.append({
            "type": "Job",
            "role": entry.title,
            "company": entry.get("author", "Company"),
            "location": "India",
            "pay": "₹35,000+/month",
            "desc": "Engineering job opportunity for freshers and experienced candidates."
        })

        if len(jobs) >= 5:
            break

    return jobs

# -------- INTERNSHIPS (Indeed RSS) --------
def fetch_internships():
    feed = feedparser.parse(
        "https://www.indeed.com/rss?q=internship+software&l=India"
    )

    internships = []
    for entry in feed.entries:
        published = datetime(*entry.published_parsed[:6])
        if not is_last_24_hours(published):
            continue

        internships.append({
            "type": "Internship",
            "role": entry.title,
            "company": entry.get("author", "Company"),
            "location": "India",
            "pay": "₹5,000–₹30,000/month",
            "desc": "Paid internship opportunity for engineering students."
        })

        if len(internships) >= 5:
            break

    return internships

# -------- HACKATHONS (SAFE MODE) --------
def fetch_hackathons():
    hackathons = []

    try:
        url = "https://unstop.com/api/public/opportunity/search"
        payload = {"opportunity": "hackathons", "page": 1}
        headers = {"User-Agent": "Mozilla/5.0"}

        r = requests.post(url, json=payload, headers=headers, timeout=10)

        if not r.headers.get("content-type", "").startswith("application/json"):
            return []

        data = r.json()

        for item in data.get("data", {}).get("data", []):
            post_time = datetime.fromtimestamp(item.get("published_at", 0))
            if not is_last_24_hours(post_time):
                continue

            hackathons.append({
                "type": "Hackathon",
                "role": item.get("title", "Hackathon"),
                "company": item.get("organisation", {}).get("name", "Organizer"),
                "location": "Online",
                "pay": "Prizes + Certificates",
                "desc": "Hackathon for engineering students to build innovative tech solutions."
            })

            if len(hackathons) >= 5:
                break

    except:
        return []

    return hackathons
