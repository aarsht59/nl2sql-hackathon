def is_safe_sql(query):
    forbidden = ["insert", "update", "delete", "drop", "alter"]

    q = query.lower()
    for word in forbidden:
        if word in q:
            return False

    return q.strip().startswith("select")