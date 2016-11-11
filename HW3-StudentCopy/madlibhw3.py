import nltk 
import random
from nltk.book import *

print("START*******")

#prints the first 150 tokens of the original text
tokens = text2[:150]
print(tokens)


tagged_tokens = nltk.pos_tag(tokens)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "NNP":"a proper noun"}
substitution_probabilities = {"NN":.15,"NNS":.10,"VB":.10,"JJ":.10, "NNP":.10}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))

print("\n\nEND*******")





