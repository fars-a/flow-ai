from fastapi import FastAPI
from search import search_duckduckgo

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Agent is running"}

@app.get("/ask")
def ask(query: str):
    results = search_duckduckgo(query)

    # Step 1: Filter important results
    filtered = []
    for r in results:
        title = r["title"].lower()
        if "best" in title or "top" in title:
            filtered.append(r)

    # Step 2: Generate recommendation
    if filtered:
        recommendation = f"Based on search results, check: {filtered[0]['title']}"
    else:
        recommendation = "No strong recommendation found, explore top results."

    return {
        "query": query,
        "results": results,
        "analysis": filtered[:3],
        "recommendation": recommendation
    }