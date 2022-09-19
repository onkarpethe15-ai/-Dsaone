def solve(n, nums, k):
    count = 0
    for i in range(n):
        if nums[i] == k:
            count = count+1
    return count
