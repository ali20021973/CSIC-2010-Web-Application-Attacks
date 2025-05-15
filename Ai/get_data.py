import mysql.connector
import time
import json
from datetime import datetime

DATA_FILE = "telescope_entries.json"
POLL_INTERVAL = 10  # seconds

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            database='Air_Condition'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None

def fetch_data(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM telescope_entries ORDER BY uuid ASC")
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except mysql.connector.Error as err:
        print(f"Query Error: {err}")
        return []

def json_datetime_converter(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError(f"Type {type(o)} not serializable")

def load_existing_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False, default=json_datetime_converter)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Updated file with new records.")

def main():
    connection = connect_to_db()
    if not connection:
        return

    all_data = load_existing_data()
    existing_uuids = {entry['uuid'] for entry in all_data}  # track known uuids

    try:
        while True:
            records = fetch_data(connection)

            # Filter new records only
            new_records = [row for row in records if row['uuid'] not in existing_uuids]

            if new_records:
                all_data.extend(new_records)
                for row in new_records:
                    existing_uuids.add(row['uuid'])
                save_data(all_data)
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] No new records.")

            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("Stopped by user.")
    finally:
        connection.close()

if __name__ == "__main__":
    main()
