def fix_grammar(text):

    ## unnecessary space removal
    words = text.split()

    for word in words:
        if word 

    return " ".Join(words)


def remove_duplicate_words(text):
    words = text.split()
    unique_words = []

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    return " ".join(unique_words)