def format_ambiguity_results(ambiguity_tuple):
    is_ambiguous, word_meanings = ambiguity_tuple
    if not is_ambiguous:
        return "No ambiguity detected."

    output = ""
    for word, meanings in word_meanings.items():
        output += f"\n🔹 Word: {word}\n"
        for i, meaning in enumerate(meanings, 1):
            output += f"   {i}. {meaning}\n"
    return output