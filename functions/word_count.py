def word_count(words):
    counts = {}

    for word in words:
        if word in counts:
            count[word] += 1
        else:
            count[word] = 1
    return counts