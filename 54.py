
# Array pair sum

def sum_pair(arr, k):

    if len(arr)<2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target, num), max(target, num)))

    print "\n".join(map(str, list(output)))

sum_pair([1,3,2,2], 4)
