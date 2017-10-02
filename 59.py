

# Reverse a string


def reverse(str):

    length = len(str)
    word = []
    spaces = [" "]

    i = 0

    while i < length:
        if str[i] not in spaces:
            word_start = i

            while i<length and str[i] not in spaces:
                i += 1
            word.append(str[word_start:i])

        i+=1

    return " ".join(reversed(word))

print reverse("    man this is")
