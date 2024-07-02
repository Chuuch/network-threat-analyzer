import os
import socket
import subprocess
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

subprocess.call('clear', shell=True)

target = input("Enter the target IP address or hostname: ")

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

def port_scan(target):
    try:

        ip = socket.gethostbyname(target)

        check_abuse_ipdb(ip)

        print("-" * 50)
        print("Scanning target:", ip)
        print("Time started:", datetime.now())
        print("-" * 50)

        for port in range(1, 65635):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")

    except socket.error:
        print("Could not connect to the server.")

port_scan(target)
