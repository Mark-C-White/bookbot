def get_num_words(string):
        words = string.split()
        return len(words)

def get_character_count(string):
    lower_case_string = string.lower()
    char_count = {}
    for char in lower_case_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dict):
    temp_list = []
    for i in dict:
        if i.isalpha():
            temp_list.append({"name": i, "num": dict[i]})
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list