
#Largest continuos sum


def large_cont(arr):
    if len(arr) == 0:
        return 0

    current_sum = max_sum = arr[0]

    for num in arr[1: ]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

print large_cont([1,2,-1,3,4,10,10,-10,-1])
