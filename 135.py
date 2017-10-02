
#Selection sort

def sel_sort(l):
    for start in range(len(l)):

        minpos = start

        for i in range(start, len(l)):

            if l[i] < l[minpos]:
                minpos = i

        (l[start], l[minpos]) = (l[minpos], l[start])

    return l

print sel_sort([74, 32, 89, 55, 21, 64])
