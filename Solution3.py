numbers = [-1,1,0,-3,3]
numbers1 = [1,2,3,4]
numbers2 = [0, 0, 3, 1]

# O(N) Time | O(1) Space
# This function calculates the previous product and store it in the result, then does the same from right to left
def productExceptSelf(nums):
    result = [1] * len(nums)
    prev = 1
    post = 1
    for i in range(len(nums)):
        result[i] *= prev
        prev *= nums[i]
        result[len(nums) - i - 1] *= post
        post *= nums[len(nums) - i - 1]

    return result

print(productExceptSelf(numbers1))