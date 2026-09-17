def word_count(list_of_words):
    counts = {}

    for word in list_of_words:
        if word in counts:
            count[word] += 1
        else:
            count[word] = 1
    return counts

def word_count2(words):
    counts = {}

    for word in words:
        counts.setdefault(word, 0)
        counts[word] += 1
        
    return counts