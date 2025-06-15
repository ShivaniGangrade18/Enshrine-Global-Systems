import requests

def check_bitcoin_drop(threshold_percent=5):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        change = data['bitcoin']['usd_24h_change']
        print(f"24h BTC Change: {change:.2f}%")

        return change <= -threshold_percent, round(change, 2)
    except Exception as e:
        print("Error fetching Bitcoin price:", e)
        return False, None
