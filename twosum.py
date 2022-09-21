# this is code for two zum
nums = [5, 7, 8, 3]
target = 11
m = {}
for i, el in enumerate(nums):
    if target-el in m:
        print([m[target-el], i])
        print(m)
    m[el] = i
# print(m)
