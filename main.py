def main():
	book_path = "books/frankenstein.txt"
	text = read_books(book_path)
	num_words = get_num_words(text)
	text_lower = text.lower()
	character_dict = get_num_characters(text_lower)
	list = dict_list(character_dict)
	sorted_list = sort_character_list(list)
	print(f"--- Begin report of {book_path} ---")
	print(f"{num_words} found in this document")
	printing(sorted_list)

def read_books(book_path):
	with open(book_path) as f:
		return f.read()
		
def get_num_words(text):
	words = text.split()
	word_count = len(words)
	return word_count

def get_num_characters(text_lower):
	character_dict = {}
	for character in text_lower:
		if character in character_dict:
			character_dict[character] += 1
		else:
			character_dict[character] = 1
	return character_dict

def dict_list(character_dict):
	character_list = []
	for key in character_dict:
		if key.isalpha() == True:
			character_list.append({"char": key, "num": character_dict[key]})
	return character_list

def sort_on(dict):
	return dict["num"]

def sort_character_list(list):
	list.sort(reverse=True, key=sort_on)
	return list

def printing(list):
	for x in list:
		print(f"The '{x["char"]}' character was found {x["num"]} times") 

main()
