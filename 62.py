

#String Compression

def compress(str):

    d = dict()

    for letter in str:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1


    for i, j in d.items():
        print i,j,


compress("AAABBBBBBaa")
