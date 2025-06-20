def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    lowercase = text.lower()
    char = {}

    for c in lowercase:
        if c in char:
            char[c] += 1
        else:
            char[c] = 1
    
    return char

def sort_on(items):
    return items["num"]

def get_sorted_list(d):
    new_list = []

    for key, value in d.items():
        if key.isalpha():
            new_list.append({"char": key, "num": value})

    new_list.sort(reverse=True, key=sort_on)
    return new_list