

#print range(9,1,-1)

def reverse(arr):
    lastindex = len(arr)-1
    for i in range(len(arr)):

        if i < lastindex:
            temp = arr[i]
            arr[i] = arr[lastindex]
            arr[lastindex] = temp
            i+=1
            lastindex-=1
        else:
            break

    return arr

print reverse([5,6,9,8,9, 100, 210])
