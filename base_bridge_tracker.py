# base_bridge_tracker.py
# Simple Base ↔ Ethereum bridge volume fetcher example

import requests

def get_bridge_volume():
    url = "https://api.llama.fi/bridges/base"
    data = requests.get(url).json()
    print("Base Bridge 24h Volume (USD):", data["bridges"][0]["volumeUSD24h"])

if __name__ == "__main__":
    get_bridge_volume()
