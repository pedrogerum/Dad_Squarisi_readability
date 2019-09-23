# Python3 program to count vowels 
# in a string 

import unidecode
import numpy as np
 
# Function to check the Vowel 
def isVowel(ch): 
    return ch.upper() in ['A', 'E', 'I', 'O', 'U'] 
  
# Returns count of vowels in str  
def countSyllable(word): 
    if isVowel(word[0]):
    	count = 1
    else:
    	count = 0


    for i in range(1,len(word)): 
        # Check for vowel 
        if (isVowel(word[i]) and not isVowel(word[i-1])): 
            count += 1

        if word[i].upper() == 'A' and word[i-1].upper() == 'I':
        	count+=1

        if word[i].upper() == 'E' and word[i-1].upper() == 'O':
        	count+=1

    return count 

def split_line(text):

	# split the text
	words = text.split()
	word_list = []
	for each_word in words:
		word_list.append(each_word)
	return(word_list)

# Main
  
# string object 
def syllable_metrics(text):
	str = text
	unaccented_string = unidecode.unidecode(str)

	# Total number of Vowels 
	words_sep = split_line(unaccented_string)
	number_syll = [countSyllable(item) for item in words_sep]

	monosyl = sum(1 for item in number_syll if item == 1)
	disyla = sum(1 for item in number_syll if item == 2)
	trisyl = sum(1 for item in number_syll if item == 3)
	polisyl = len(number_syll) - trisyl - disyla - monosyl
	print("There are %d monosyl, %d disyla, %d trisyla, and %d polisyl" %(monosyl, disyla, trisyl, polisyl))

	return monosyl, disyla, trisyl, polisyl

  

def sentence_number(text):

	words_sep = split_line(text)
	sentence_count = 0
	sentence_end = {'?', '!', '.'}
	space = {' '}
	word_per_sentence = []

	print(words_sep)
	add_word = 0
	for item in text:
		if item in space:
			add_word += 1
		elif item in sentence_end:
			word_per_sentence.append(add_word)
			add_word = 0

	word_per_sentence[0]+=1		

	print("Words per sentence", word_per_sentence)

	sentence_count = sum(1 for item in text if item in sentence_end)

	if sentence_count == 0:
		sentence_count += 1

	mean_word_per_sentence =  len(words_sep)/sentence_count
	mean_word_per_sentence_check = np.mean(word_per_sentence)
	print("Sentence count is %d and mean_word_per_sentence is %d" %(sentence_count, mean_word_per_sentence))
	print("checking mean word per sentence: ", mean_word_per_sentence_check)

	return sentence_count, mean_word_per_sentence


def dad_squarisi_test(text):

	sentence_count, mean_word_per_sentence = sentence_number(text)
	monosyl, disyla, trisyl, polisyl = syllable_metrics(text)

	leg_index = 0.4*(mean_word_per_sentence + polisyl)

	return leg_index


f = open('children_1.txt', 'r')
content = f.read()
print(content)
f.close()

a = dad_squarisi_test(content)
print(a)
# by SamyuktaSHegde