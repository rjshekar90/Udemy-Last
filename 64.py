

# Unique chars in a string

def unique(str):

    lst = []
    for i in str:
        lst.append(i)


    d = dict()
    for letter in lst:
        if letter in d:
            d[letter] +=  1
        else:
            d[letter] = 1

    for k, v in d.items():
        if v > 1:
            return False
    return True


print unique("abcde")
