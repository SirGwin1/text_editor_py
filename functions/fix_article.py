def fix_articles(text):
    words = text.split()
    vowels = "aeiouAEIOU"

    for i, word in enumerate(words):

        if word in ("a", "an") and i + 1 < len(words):

            next_word = words[i + 1]

            if next_word[0] in vowels:
                words[i] = "an"
            else:
                words[i] = "a"

    return " ".join(words)