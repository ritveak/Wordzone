from nltk.corpus import words
from collections import defaultdict
from wordfreq import zipf_frequency
import pickle

frequency_wordlist_map = defaultdict(list)
# a=1
for word in words.words():
  frequency_wordlist_map[zipf_frequency(word, 'en')].append(word)
  # a=a+1
  # if(a<15):
  #   print(word+"-"+str(zipf_frequency(word, 'en')))

with open('corpus_data/frequenc_words.pkl', 'wb') as f:
  pickle.dump(frequency_wordlist_map, f)