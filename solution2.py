numbers = [-1,1,0,-3,3]
numbers1 = [1,2,3,4]
numbers2 = [0, 0, 3, 1]

# O(N) Time | O(1) Space
# This function calculates the total product (mcm) if the array, without zeroes. If there is one zero, it marks it with a flag, cause every other integer in the
# array will have a result of zero. If there are 2 zeroes, it stops calculating since every result will be zero. After that, for each number
# in the array, it multiplies the mcm by the inverse of said number (this is equivalent to divide it by the number but not a division itself)
def productExceptSelf(nums):
    result = []
    mcm = 1
    flag = False
    for i in range(len(nums)):
        if nums[i] == 0 and not flag:
            flag = True
            continue
        elif nums[i] == 0 and flag:
            mcm = 0
            break
        else:
            mcm *= nums[i]
    mcm = int(mcm)
    for j in range(len(nums)):
        if nums[j] == 0:
            excluded = mcm
        elif flag:
            excluded = 0
        else:
            excluded = int(mcm * nums[j] ** (-1))
        result.append(excluded)

    return result

print(productExceptSelf(numbers2))