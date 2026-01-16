from schema import get_tables
from planner import generate_reasoning_plan
from sql_generator import generate_sql
from safety import is_safe_sql
from db import run_query
from ambiguity import is_ambiguous
from meta import is_meta_query
from meta_handler import handle_meta_query

print("🔥 PROGRAM STARTED")

# 1️⃣ Take user input
question = input("❓ Ask your question: ")
print("🧠 User Question:", question)

# 2️⃣ Ambiguity check (FIX 2 – CORRECT PLACE)
if is_ambiguous(question):
    print("⚠️ Question is ambiguous. Please clarify.")
    print("👉 Example: last 7 days, top 5, highest revenue, etc.")
    exit()

# 3️⃣ Load schema
tables = get_tables()
print("📦 Tables loaded")

# 4️⃣ Reasoning
reasoning = generate_reasoning_plan(question, tables)
print("\n🧠 Reasoning Trace:")
for step in reasoning:
    print("•", step)

# 5️⃣ SQL generation
sql = generate_sql(question)
print("\n🧾 Generated SQL:", sql)

if sql is None:
    print("❌ SQL generation failed")
    exit()

# 6️⃣ Safety check + execution
if is_safe_sql(sql):
    result = run_query(sql)
    print("\n✅ Answer:", result)
else:
    print("🚨 Unsafe SQL blocked")
   