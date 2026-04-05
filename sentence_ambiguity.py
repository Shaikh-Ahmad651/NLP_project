def detect_ambiguity(text):
    # For demo, a fixed dictionary of ambiguous words
    AMBIGUOUS_WORDS = {
        "bank": ["financial institution", "river bank", "pile of something"],
        "bat": ["flying mammal", "sports equipment"]
    }

    words = text.lower().split()
    ambiguous = {}
    for w in words:
        if w in AMBIGUOUS_WORDS:
            ambiguous[w] = AMBIGUOUS_WORDS[w]

    is_ambiguous = len(ambiguous) > 0
    return is_ambiguous, ambiguous   # tuple: True/False + dict