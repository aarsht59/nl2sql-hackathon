def is_meta_query(question):
    q = question.lower()

    if "table" in q and "exist" in q:
        return "list_tables"

    if "schema" in q:
        return "table_schema"

    if "most rows" in q or "largest table" in q:
        return "largest_table"

    return None