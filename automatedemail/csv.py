import os
import csv
from django.conf import settings
from datetime import datetime

def get_email_ids_from_csv(file_name='emails.csv'):
    file_path = os.path.join(settings.BASE_DIR, file_name)

    email_ids = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                email_ids.append(row["email"])  # Ensure "email" matches the column name in CSV
    except FileNotFoundError:
        print(f"Error: File {file_path} not found!")
    return email_ids





def log_email_status(file_path, email, status):
    """Log email status to a CSV file."""
    file_exists = os.path.isfile(file_path)

    # Ensure the directory exists and create if necessary
    dir_path = os.path.dirname(file_path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Email", "Status", "Timestamp"])  
        writer.writerow([email, status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])