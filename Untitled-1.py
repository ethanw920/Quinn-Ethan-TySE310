
import requests

# API keys
NEWSAPI_KEY = "1d2e03011ba34a2e9c8d5569bbc3bf96"
GNEWS_KEY = "b0f02ecab335f88ff8452323b66c88e0"
NEWSDATA_KEY = "pub_1d5c551fece94f7887d88e21c17e051a"

def fetch_newsapi(query):
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize=5&apiKey={NEWSAPI_KEY}"
    resp = requests.get(url)
    data = resp.json()
    return {"NewsAPI": data.get("articles") or data}

def fetch_gnews(query):
    url = f"https://gnews.io/api/v4/search?q={query}&max=5&token={GNEWS_KEY}"
    resp = requests.get(url)
    data = resp.json()
    return {"GNews": data.get("articles") or data}

def fetch_newsdataapi(query):
    url = f"https://newsdata.io/api/1/news?apikey={NEWSDATA_KEY}&q={query}&language=en"
    resp = requests.get(url)
    data = resp.json()
    return {"NewsDataAPI": data.get("results") or data}

def main():
    query = input("Enter a search term: ")

    results = [
        fetch_newsapi(query),
        fetch_gnews(query),
        fetch_newsdataapi(query)
    ]

    for result in results:
        for source, articles in result.items():
            print(f"\nTop results from {source}:")

            if isinstance(articles, list):
                if len(articles) == 0:
                    print("No results found.")
                for i, article in enumerate(articles[:5], start=1):
                    title = article.get("title", "No title")
                    link = article.get("link") or article.get("url", "No URL")
                    print(f"{i}. {title} ({link})")
            else:
                # Not a list, print whole result
                print(articles)

if __name__ == "__main__":
    main()
