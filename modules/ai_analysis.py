# modules/ai_analysis.py

def analyze(results):
    filtered = []

    for r in results:
        title = r["title"].lower()
        if "best" in title or "top" in title:
            filtered.append(r)

    return filtered[:3]


def generate_recommendation(filtered):
    if filtered:
        return f"Based on search results, check: {filtered[0]['title']}"
    return "No strong recommendation found, explore top results."