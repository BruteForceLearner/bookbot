def get_num_words(text):
    count = len(text.split())
    return count

#?
def get_chars_dict(text):
    counts = {}
    for character in text.lower():
        if character in counts:
            counts[character] = counts[character] + 1
        else: 
            counts[character] = 1
    return counts
#?