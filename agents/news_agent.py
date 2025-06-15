import requests

def fetch_bitcoin_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "bitcoin",
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": "deb0593e05db472baefcb04ebc2e6306",  # Your API Key
        "pageSize": 5
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        urls = [article["url"] for article in articles if "url" in article]
        return urls
    else:
        print(f"News API error: {response.status_code}")
        return []
