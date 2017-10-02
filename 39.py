

import timeit
def sum1(n):
    final_sum = 0
    for i in xrange(n+1):
        final_sum += i

    return final_sum

print sum1(10)

print timeit(sum1)
