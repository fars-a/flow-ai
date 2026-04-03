import requests
from bs4 import BeautifulSoup

def search_duckduckgo(query):
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

        if "duckduckgo.com" in link:
            continue


        results.append({
            "title": title,
            "link": link
        })

    return results[:5]