import requests
import csv
import os
import time
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

park_id = "f95d7f76-2024-4510-b799-26e122d0e448"

url = f"https://api.themeparks.wiki/v1/entity/{park_id}/live"

csv_file = Path(__file__).resolve().parent.parent / "data" / "production" / "wait_times.csv"
csv_file.parent.mkdir(parents=True, exist_ok=True)


def collect_wait_times():
    print("Starting collection...")
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

    except requests.RequestException as error:
        print("Error collecting data:", error)
        return

    is_open = any(
        entity["entityType"] == "ATTRACTION"
        and entity["status"] == "OPERATING"
        for entity in data["liveData"]
    )

    if not is_open:
        print("USS is currently closed. No data collected.")
        return

    timestamp = datetime.now(
        ZoneInfo("Asia/Singapore")
    ).strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(csv_file)

    with open(csv_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "attraction",
                "wait_time",
                "status"
            ])

        for entity in data["liveData"]:
            if entity["entityType"] == "ATTRACTION":
                name = entity["name"]
                status = entity["status"]

                if "queue" in entity and "STANDBY" in entity["queue"]:
                    wait_time = entity["queue"]["STANDBY"]["waitTime"]
                else:
                    wait_time = None

                writer.writerow([
                    timestamp,
                    name,
                    wait_time,
                    status
                ])

                print(
                    timestamp,
                    "|",
                    name,
                    "|",
                    wait_time,
                    "|",
                    status
                )

        file.flush()
        os.fsync(file.fileno())

def main():
    try:
        while True:
            collect_wait_times()
            print("Waiting 5 minutes...")
            time.sleep(300)
    except KeyboardInterrupt:
        print("Collection stopped.")

if __name__ == "__main__":
    main()