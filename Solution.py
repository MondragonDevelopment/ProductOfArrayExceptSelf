numbers = [-1,1,0,-3,3]

# O(N^2) Time
def productExceptSelf(nums):
    result = []

    for j in range(len(nums)):
        mem = nums[j]
        nums[j] = 1
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        result.append(product)
        nums[j] = mem
    return result

print(productExceptSelf(numbers))