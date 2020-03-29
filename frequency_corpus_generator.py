from nltk.corpus import words
from collections import defaultdict
from wordfreq import word_frequency
import pickle

frequency_wordlist_map = defaultdict(list)
for word in words:
  frequency_wordlist_map[word_frequency(word)].append(word)

with open('corpus_data/frequenc_words.pkl', 'wb') as f:
  pickle.dump(frequency_wordlist_map, f)