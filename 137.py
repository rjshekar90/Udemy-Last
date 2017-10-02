
#nptel

# insertion sort

def insertion_sort(l):

    for sliceEnd in range(len(l)):
        pos = sliceEnd

        while pos > 0 and l[pos] < l[pos-1]:
            (l[pos], l[pos-1]) = (l[pos-1], l[pos])
            pos = pos-1

    return l

print insertion_sort([74, 32, 89, 55, 25, 64])
