import nltk
import re
from nltk.tokenize import word_tokenize


def gopher_quality_filter(text: str) -> bool:

    words = word_tokenize(text)
    if len(words) <= 50 or len(words) >= 100000:
        return False
    
    word_lengths = [len(word) for word in words if word.isalpha()]
    if not word_lengths: return False
    avg_word_length = sum(word_lengths) / len(word_lengths)
    if avg_word_length < 3 or avg_word_length > 10:
        return False

    lines = text.splitlines()
    count = 0
    for line in lines:
        if line.endswith("..."):
            count += 1
    if count > 0 and (count / len(lines)) > 0.3:
        return False

    alpha_words = 0
    for word in words:
        if re.search(r'^[A-Za-z]', word):
            alpha_words += 1
    if (alpha_words / len(words)) < 0.2:
        return False

    return True