def is_ambiguous(question):
    q = question.lower()

    ambiguous_words = [
        "recent",
        "latest",
        "best",
        "top",
        "highest",
        "lowest"
    ]

    for word in ambiguous_words:
        if word in q:
            return True

    return False