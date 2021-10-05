import re
from collections import Counter
def word_count(phrase):
    words = re.findall('[a-z\d]+', phrase.lower())
    return dict(Counter(words))
