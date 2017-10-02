
#Reverse a string

def reverse(s):

    words = []
    length = len(s)
    spaces = [" "]

    i = 0

    if length == 0:
        return ""
    if length == 1 :
        return s  

    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])
        i+=1

    return " ".join(map(str, list(reversed(words))))

print reverse('   Hello John    how are you   ')
