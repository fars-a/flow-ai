# modules/web_search.py
import requests
from bs4 import BeautifulSoup

def perform_search(query, max_results=5):
    url = "https://html.duckduckgo.com/html/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    data = {
        "q": query
    }

    response = requests.post(url, headers=headers, data=data)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.find_all("a", class_="result__a"):
        title = result.get_text()
        link = result.get("href")

        # remove ads / junk
        if "duckduckgo.com" in link:
            continue

        results.append({
            "title": title,
            "link": link
        })

    return results[:max_results]