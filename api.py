import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def check_abuse_ipdb(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    params = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['data']['abuseConfidenceScore'] > 0:
            print(f"IP {ip} found on AbuseIPDB with a confidence score of {data['data']['abuseConfidenceScore']}.")
        else:
            print(f"IP {ip} is not found on AbuseIPDB.")
    else:
        print("Failed to connect to AbuseIPDB API. Please check your API key and network connection.")
