

#Anagrams
def anagram(str1, str2):

    l1 = []
    l2 = []

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    print str1
    print str2

    s1 = sorted(str1)
    s2 = sorted(str2)

    d = dict()

    for letter in s1:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    for letter in s2:
        if letter in d:
            d[letter] -= 1
        else:
            d[letter] = 1

    for k,v in d.items():
        if v != 0:
            return False

    return True




print anagram("clint eastwood", "old West action")
