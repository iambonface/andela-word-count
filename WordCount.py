"""
	Function that counts frequency of words in a sentence

	Arg:
		String

	Result:
	    Dictionary with key value pair. key is the string and value the frequency of occurance
"""

def word_count(my_string):
	if isinstance(my_string, str):
		word_split =  my_string.split()

		my_dict = {}

		for w in word_split:
			my_dict[w] = word_split.count(w)

		return my_dic

	

	else:
		raise ValueError("Invalid")
