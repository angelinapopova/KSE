import random
import string
import nltk
from nltk.corpus import words, wordnet
from nltk import pos_tag

nltk.download("wordnet")
nltk.download("words")

def generate_word():
    word_list = words.words()
    filtered_words = [word for word in word_list if word.isalpha() and (len(word) == 5)]
    noun_words = [word for word in filtered_words if wordnet.synsets(word, pos= wordnet.NOUN)]
    
    return random.choice(noun_words)


