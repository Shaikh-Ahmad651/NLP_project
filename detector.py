from preprocess import sentence_split, word_split, remove_stopwords, lemmatize_words, get_wordnet_meanings

def detect_word_ambiguity(text):
    result = {}
    sentences = sentence_split(text)

    for sentence in sentences:
        words = word_split(sentence) 
        filtered = remove_stopwords(words)
        lemmatized = lemmatize_words(filtered)

        for word in lemmatized:
            if not word.isalpha():
                continue

            meanings = get_wordnet_meanings(word)

            if len(meanings) > 1:
                result[word] = meanings[:4]

    is_ambiguous = len(result) > 0
    return is_ambiguous, result