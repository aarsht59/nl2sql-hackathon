from schema import get_tables, get_table_schema, get_table_row_count

def handle_meta_query(meta_type, question):
    if meta_type == "list_tables":
        tables = get_tables()
        print("📦 Tables in database:")
        for t in tables:
            print("-", t)

    elif meta_type == "table_schema":
        words = question.split()
        table_name = None

        for w in words:
            if w[0].isupper():
                table_name = w
                break

        if not table_name:
            print("❌ Please specify table name (e.g. Invoice)")
            return

        schema = get_table_schema(table_name)
        print(f"🧱 Schema of {table_name}:")
        for col in schema:
            print(col)

    elif meta_type == "largest_table":
        tables = get_tables()
        max_table = None
        max_count = 0

        for t in tables:
            count = get_table_row_count(t)
            if count > max_count:
                max_count = count
                max_table = t

        print(f"🏆 Table with most rows: {max_table} ({max_count} rows)")