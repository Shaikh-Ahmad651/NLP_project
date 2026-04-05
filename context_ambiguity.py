from sentence_transformers import SentenceTransformer, util
from preprocess import get_wordnet_meanings
import torch


model = SentenceTransformer('BAAI/bge-base-en-v1.5')

def detect_contextual_ambiguity(sentence, threshold=0.45
                                ):
    """
    Detects ambiguity by comparing the sentence context 
    to WordNet definitions using Cosine Similarity.
    """
    # Use a basic split or a proper tokenizer from preprocess
    words = sentence.split()
    ambiguous_words = {}

    for word in words:
        # Clean word (remove punctuation)
        clean_word = "".join(char for char in word if char.isalpha())
        if not clean_word:
            continue

        meanings = get_wordnet_meanings(clean_word)
        if len(meanings) < 2:
            continue  # Not ambiguous if only 1 dictionary meaning

        # 1. Encode the full sentence to get context
        sentence_emb = model.encode(sentence, convert_to_tensor=True)

        # 2. Encode all dictionary meanings for that word
        meaning_embs = model.encode(meanings, convert_to_tensor=True)

        # 3. Calculate Cosine Similarity between context and meanings
        # sims is a tensor of scores (e.g., [0.12, 0.55, 0.08...])
        sims = util.cos_sim(sentence_emb, meaning_embs)[0]

        # 4. Filter: Only keep meanings that are mathematically "close" to the sentence
        valid_meanings = []
        for i, score in enumerate(sims):
            if score >= threshold:
                valid_meanings.append(meanings[i])

        # If more than one meaning fits the context, it's contextually ambiguous
        if len(valid_meanings) > 1:
            # We limit to the top 5 most relevant ambiguous meanings to keep output clean
            ambiguous_words[clean_word] = valid_meanings[:5]

    is_ambiguous = len(ambiguous_words) > 0
    return is_ambiguous, ambiguous_words