def number_base_converter(text):

    words = text.split()

    result = []

    for word in words:
        if word == "(hex)":
            result[-1] = str(int(result[-1], 16))

        elif word == "(bin)":
            result[-1] = str(int(result[-1], 2))

        else:
            result.append(word)

    return " ".join(result)