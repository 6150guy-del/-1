"""Simple text statistics utility."""

import re
from collections import Counter


def word_count(text):
    """Return the number of words in text."""
    return len(text.split())


def char_count(text, include_spaces=True):
    """Return the number of characters in text."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def sentence_count(text):
    """Return the number of sentences in text."""
    segments = re.split(r'[.!?]+', text)
    return sum(1 for s in segments if s.strip())


def average_word_length(text):
    """Return the average word length in text."""
    words = text.split()
    if not words:
        return 0.0
    return sum(len(w.strip(".,!?;:\"'")) for w in words) / len(words)


def most_common_words(text, n=5):
    """Return the n most common words (case-insensitive) as a list of (word, count) tuples.

    # TODO: strip punctuation from each word before counting and ignore
    # common stop words: 'the', 'a', 'an', 'is', 'in', 'it', 'of', 'and', 'to'.
    """
    pass


def summarize(text):
    """Print a brief summary of text statistics."""
    print(f"Words:         {word_count(text)}")
    print(f"Characters:    {char_count(text)}")
    print(f"Sentences:     {sentence_count(text)}")
    print(f"Avg word len:  {average_word_length(text):.2f}")
    top = most_common_words(text)
    if top:
        print(f"Top words:     {', '.join(f'{w}({c})' for w, c in top)}")
