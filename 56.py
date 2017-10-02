
# find the missing element

def finder(lst1, lst2):

    d = dict()

    for num in lst1:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    for num in lst2:
        if num in d:
            d[num] -= 1

    for k,v in d.items():
        if v!=0:
            print k

finder([1,2,3,4,5,10], [1,3,2,4,5])
