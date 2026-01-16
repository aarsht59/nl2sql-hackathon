def generate_reasoning_plan(question, tables):
    plan = []

    plan.append(f"User wants: {question}")
    plan.append("First, identify relevant tables from schema.")

    if "customer" in question.lower():
        plan.append("Customer-related question → Customer table needed")

    if "country" in question.lower() or "brazil" in question.lower():
        plan.append("Country info exists in Customer table")

    plan.append("Count matching rows instead of selecting all data")
    plan.append("Generate safe SELECT COUNT query")

    return plan