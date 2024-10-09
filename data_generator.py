import random
import nltk 
from nltk.corpus import words

nltk.download('words')

word_list = words.words()

num_words = 100000

random_words = random.choices(word_list, k=num_words)

with open('random_words.txt', 'w') as f:
    for word in random_words:
        f.write(word + '\n')

