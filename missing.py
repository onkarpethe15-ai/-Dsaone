Given an array arr containing n distinct numbers in the range [0, n+1], return the only two numbers in the range that is missing from the array in non-decreasing order.
def solve(n, arr):
    # CODE HERE
    l = []
    for i in range(0, n+2):
        if i not in arr:
            l.append(i)
    return l
