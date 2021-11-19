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

def currencyTickerLowercase(currency, ticker):
    return ticker.lower() + currency.lower()

def currencyTickerUppercase(currency, ticker):
    return ticker.upper() + currency.upper()

def tickerPrice(currency, ticker):
    lcTicker = currencyTickerLowercase(currency, ticker)
    tickerData = wazirClient.send("historical_trades",
                {"limit": 10, "symbol": lcTicker, "recvWindow": 10000, "timestamp": int(time.time() * 1000)}
                )
    
    tickerPrice_parsed = tickerData[1][1]
    tickerPriceRec = tickerPrice_parsed.get("price")
    return tickerPriceRec

def PriceBreakoutAlert(currency, ticker, alertPrice):
    while True:
        currentPrice = tickerPrice(currency, ticker)
        if (currentPrice == alertPrice):
            ucCurrency = currency.upper()
            ucTicker = ticker.upper()
            return f"{ucTicker}({ucCurrency}) has hit {alertPrice}!"
