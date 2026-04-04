# modules/query_handler.py

def get_query_from_request(request):
    """
    Extracts query string from incoming request JSON.
    """
    data = await request.json()
    query = data.get("query", "")
    return query