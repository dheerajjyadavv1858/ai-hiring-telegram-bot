import json
import os

FILE_NAME = "posted.json"

def load_posted():
    if not os.path.exists(FILE_NAME):
        return set()
    with open(FILE_NAME, "r") as f:
        return set(json.load(f))

def save_posted(posted_set):
    with open(FILE_NAME, "w") as f:
        json.dump(list(posted_set), f)

def is_duplicate(unique_id, posted_set):
    return unique_id in posted_set

def mark_posted(unique_id, posted_set):
    posted_set.add(unique_id)
