# 
# File Header
#
# Define vowels

vowels = "aeiouAEIOU"

# Loop through word, one letter at a time
def piggy(word):
	n=0
	endword=""
	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			if n==0:
				# True?  We are done
				pig = word + "yay"
				return pig
			else: 
				pig= word[n:] + endword + "ay"
				return pig
		else:
			endword = endword + word[n]
			n = n + 1
			
		

# Ask for word
word = input("Please enter a word: ")
print(piggy(word))
