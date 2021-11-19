from wazirx_sapi_client.rest import Client
import time
import os

wazirClient = Client()
wazirClient = Client(api_key=os.getenv('api_key'), secret_key=os.getenv('secret_key'))

def shibPrice():
    shibData = wazirClient.send("historical_trades",
                {"limit": 10, "symbol": "shibinr", "recvWindow": 10000, "timestamp": int(time.time() * 1000)}
                )

    shibData_parsed = shibData[1][1]
    shibPriceRec = shibData_parsed.get("price")
    return shibPriceRec