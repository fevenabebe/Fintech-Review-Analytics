import re

STOPWORDS = {
    "the", "is", "in", "at", "to", "a", "and", "on", "for", "it",
    "this", "that", "with", "as", "was", "but", "be", "are", "of",
    "my", "i", "you", "we", "they", "he", "she", "them", "our"
}

def clean_text(text):

    text = str(text).lower()

    # remove punctuation/numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # tokenize
    tokens = text.split()

    # remove stopwords
    tokens = [t for t in tokens if t not in STOPWORDS]

    return ' '.join(tokens)