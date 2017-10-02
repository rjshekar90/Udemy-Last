

#reverse individual words

def reverse(s):

    l = s.split(" ")
    j = []

    for i in l:
        j.append(i[::-1])

    print " ".join(map(str, list(j)))




print reverse("hello world")
