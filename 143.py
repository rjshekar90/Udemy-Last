
# quick sort

def quick_sort(A,l,r):

    if (r-l) <= 0:
        return

    yellow = l+1

    for green in range(l+1, r):
        if A[green] <= A[l]:
            (A[yellow], A[green]) = (A[green], A[yellow])
            yellow += 1

    (A[l], A[yellow-1]) = (A[yellow-1], A[l])

    quick_sort(A,l,yellow-1)
    quick_sort(A, yellow, r)

    return A





A = [3,4,5,7,1,2,9]
print quick_sort(A, 0, len(A))
