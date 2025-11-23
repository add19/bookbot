def get_num_words_in_text(text):
    words = text.split()
    return len(words)

def get_char_freq_in_text(text):
    lowered = text.lower()
    result = {}
    for i in range(0, len(lowered)):
        if lowered[i] == ' ':
            continue
        if lowered[i] not in result:
            result[lowered[i]] = 0
        result[lowered[i]] += 1
    return result

# has to take in a dictionary of characters to their frequencies and return a sorted list of dictionaries
def sort_on(dict):
    return dict["num"]

def sort_characters_in_map(dict):
    list = []
    for character in dict:
        count = dict[character]
        kv = {}
        kv["char"] = character
        kv["num"] = count 
        list.append(kv)
    list.sort(key=sort_on, reverse=True)

    return list    
