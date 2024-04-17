import requests
import json
import time
from datetime import datetime, timedelta


jasonfile = 'rssjsonfile.json'
update_timeset = 1

def fetch_data():
    try:
        response = requests.get('https://aws.amazon.com/about-aws/whats-new/recent/feed/')
       # response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching AWS RSS feed: {e}")
        return None

def load_existing_entries():
    try:
        with open(jasonfile, 'r') as file:
            existing_entries = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_entries = []
    return existing_entries

def save_data(entries):
    with open(jasonfile, 'w') as file:
       #file.write(jasonfile)
        json.dump(entries, file)

def update_feed():
    fetched_entries = fetch_data()
    if not fetched_entries:
        return

    existing_entries = load_existing_entries()
    new_entries = [entry for entry in fetched_entries if entry not in existing_entries]

    if new_entries:
        existing_entries.extend(new_entries)
        save_data(existing_entries)
        print(f"{len(new_entries)} new entries added to the JSON file.")
    else:
        print("No new entries found.")

def main():
    while True:
        update_feed()
    #    time.sleep(60)  # 15 minutes interval (1 * 60 seconds)
        
        next_update_time = datetime.now() + timedelta(minutes=update_timeset)
        print(f"Next update in 10 sec at {next_update_time.strftime('%H:%M:%S')}")
        time.sleep(update_timeset * 60/6)

if __name__ == "__main__":
    main()
