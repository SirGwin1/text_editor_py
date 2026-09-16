def word_count(list_of_words):
    counts = {}

    for word in list_of_words:
        if word in counts:
            count[word] += 1
        else:
            count[word] = 1
    return counts