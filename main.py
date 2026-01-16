from schema import get_tables, get_table_schema
from db import run_query

print("📦 Tables in Database:")
tables = get_tables()
for t in tables:
    print("-", t)

print("\n🧱 Customer Table Schema:")
schema = get_table_schema("Customer")
for col in schema:
    print(col)

print("\n👥 Total Customers:")
result = run_query("SELECT COUNT(*) FROM Customer;")
print(result)