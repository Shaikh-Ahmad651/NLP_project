# Import WordNet from NLTK
from nltk.corpus import wordnet as wn


# 🔷 Function 1: Get meanings (synsets) of a word
def get_word_meanings(word):
    """
    Input: word (string)
    Output: list of meanings (synsets)
    """
    synsets = wn.synsets(word)  # Get all meanings of word
    return synsets


# 🔷 Function 2: Check if word is ambiguous
def is_ambiguous(word):
    """
    Input: word
    Output: True if multiple meanings exist
    """
    synsets = wn.synsets(word)

    if len(synsets) > 1:  # More than one meaning
        return True
    else:
        return False


# 🔷 Function 3: Get definitions (human-readable meanings)
def get_definitions(word):
    """
    Input: word
    Output: list of definitions
    """
    synsets = wn.synsets(word)

    definitions = []

    for syn in synsets:
        definitions.append(syn.definition())  # Extract meaning text

    return definitions