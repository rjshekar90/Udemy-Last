
# Bubble sort

#make multiple passes through the list

def bubble_sort(arr):

    for num in range(len(arr)-1, 0, -1):

        for k in range(num):
            if arr[k] > arr[k+1]:
                (arr[k], arr[k+1]) = (arr[k+1], arr[k])

    return arr
print bubble_sort([94,13,21,96,97,10,20,30])
