# preprocess.py
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def sentence_split(text):
    return sent_tokenize(text)

def word_split(text):
    return word_tokenize(text)

def remove_stopwords(words):
    return [w for w in words if w.lower() not in stop_words]

def lemmatize_words(words):
    return [lemmatizer.lemmatize(w) for w in words]

def pos_tagging(words):
    return pos_tag(words)

def get_wordnet_meanings(word):
    from nltk.corpus import wordnet as wn
    synsets = wn.synsets(word)
    
    # This sorts by how common the meaning is in real English.
    # 'Animal' and 'Baseball Bat' will now ALWAYS come before 'Poet' or 'Physics'.
    synsets = sorted(synsets, key=lambda s: sum(l.count() for l in s.lemmas()), reverse=True)
    
    # Only return the top 3 most common meanings to avoid "Dictionary Noise"
    return [s.definition() for s in synsets[:3]]