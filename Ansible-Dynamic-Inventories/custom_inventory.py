#!/usr/bin/env python

import json
import requests

def get_inventory():
    response = requests.get("https://api.example.com/hosts")
    hosts = response.json()
    inventory = {
        "all": {
            "hosts": [host['hostname'] for host in hosts],
        }
    }
    return inventory

if __name__ == "__main__":
    print(json.dumps(get_inventory()))
