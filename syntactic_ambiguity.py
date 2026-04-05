import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def detect_syntactic_ambiguity(text):
    doc = nlp(text)
    ambiguities = {}
    
    for token in doc:
        # Check for Prepositional Phrase attachment ambiguity (e.g., "with")
        if token.pos_ == "ADP": 
            phrase = "".join([t.text_with_ws for t in token.subtree]).strip()
            ambiguities["Prepositional Attachment"] = [
                f'"{phrase}" modifies the action (How you did it)',
                f'"{phrase}" modifies the noun (Who/what had it)'
            ]
            
    is_ambiguous = len(ambiguities) > 0
    return is_ambiguous, ambiguities