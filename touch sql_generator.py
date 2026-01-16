def generate_sql(question):
    q = question.lower()
    if "customer" in q and "brazil" in q:
        return """
        SELECT COUNT(*)
        FROM Customer
        WHERE Country = 'Brazil';
        """
    return None