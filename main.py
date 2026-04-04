from fastapi import FastAPI

from modules.web_search import perform_search
from modules.ai_analysis import analyze, generate_recommendation
from modules.output_formatter import format_output

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Agent is running"}

@app.get("/ask")
def ask(query: str):
    # Step 1: Search
    results = perform_search(query)

    # Step 2: Analyze
    analysis = analyze(results)

    # Step 3: Recommend
    recommendation = generate_recommendation(analysis)

    # Step 4: Format
    output = format_output(query, results, analysis, recommendation)

    return output