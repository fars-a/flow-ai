# modules/output_formatter.py
from datetime import datetime

def format_output(query, results, analysis, recommendation):
    return {
        "query": query,
        "results": results,
        "analysis": analysis,
        "recommendation": recommendation,
        "timestamp": datetime.now().isoformat()
    }