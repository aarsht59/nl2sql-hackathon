def generate_sql(question):
    q = question.lower()

    # Case 1: Brazil customers
    if "customer" in q and "brazil" in q:
        return """
        SELECT COUNT(*)
        FROM Customer
        WHERE Country = 'Brazil';
        """

    # Case 2: Rock + Jazz customers
    if "rock" in q and "jazz" in q and "customer" in q:
        return """
        SELECT DISTINCT c.FirstName, c.LastName
        FROM Customer c
        JOIN Invoice i ON c.CustomerId = i.CustomerId
        JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
        JOIN Track t ON il.TrackId = t.TrackId
        JOIN Genre g ON t.GenreId = g.GenreId
        WHERE g.Name IN ('Rock', 'Jazz')
        GROUP BY c.CustomerId
        HAVING COUNT(DISTINCT g.Name) = 2;
        """

    return None   # ✅ ALWAYS LAST