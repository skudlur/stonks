from wazirx_sapi_client.rest import Client
import time
import os

wazirClient = Client()
wazirClient = Client(api_key=os.getenv('api_key'), secret_key=os.getenv('secret_key'))

alertList = []

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

def PriceBreakoutAlertAdd(currency, ticker, alertPrice):
    alertListing = [currency, ticker, alertPrice]
    alertList.append(alertListing)
    print(alertList)
    return "Alert successfully added!"

def PriceBreakoutAlertOut():
    for i in alertList:
        iList = list(i)
        # print(tickerPrice(iList[0], iList[1]))
        # print(iList[2])
        if (float(iList[2]) <= float(tickerPrice(iList[0], iList[1]))):
            return True, i
            break
        else:
            return False
            # ucCurrency = i[0].upper()
            # ucTicker = i[1].upper()
            # alertPrice = i[2]
            # return f"{ucTicker}({ucCurrency}) has hit {alertPrice}!"
            # break

def PriceBreakoutCheckingLoop():
    # print(PriceBreakoutAlertOut())
    breakoutData = PriceBreakoutAlertOut()
    outTrueFalse = breakoutData[0]
    print(outTrueFalse)
    if (outTrueFalse):
        ucCurrency = breakoutData[1][0].upper()
        ucTicker = breakoutData[1][1].upper()
        alertPrice = breakoutData[1][2]
        return f"{ucTicker}({ucCurrency}) has hit {alertPrice}!"
    else:
        time.sleep(5)
        PriceBreakoutCheckingLoop()
    
