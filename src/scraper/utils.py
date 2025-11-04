import os
import time
import requests

def safe_request(url, delay=1):
    """Request a URL safely with a delay to avoid rate-limiting."""
    r = requests.get(url)
    time.sleep(delay)
    if r.status_code != 200:
        print(f"Failed to fetch {url} ({r.status_code})")
        return None
    return r.text

def save_text(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content)
        f.write('\n')