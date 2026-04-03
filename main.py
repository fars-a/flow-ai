from fastapi import FastAPI
from search import search_duckduckgo

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Agent is running"}

@app.get("/ask")
def ask(query: str):
    results = search_duckduckgo(query)

    # Simple analysis
    analysis = []
    for r in results:
        if "best" in r["title"].lower():
            analysis.append(r["title"])

    return {
        "query": query,
        "results": results,
        "analysis": analysis[:3]
    }