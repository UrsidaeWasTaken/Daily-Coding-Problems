"""
Given an array of integers, find the maximum possible sum you can get from a non-empty contiguous subarray in the array.
For example, given [-2, 2, 5, -11, 6], the maximum possible sum subarray should be [2, 5] and the program return 7.
"""

# Solution
def max_consecutive_sum(nums):
    highest = total = nums[0]
    for i in range(1, len(nums)):
        total = max(nums[i], nums[i] + total)
        highest = max(total, highest)
    return highest

# Custom Tests
test_inputs = [
    [-2, 2, 5, -11, 6],
    [-3, -2, -1, -4],
    [-3, 2, 1, -4],
    [1, -2, 3, -4, 5, -3, 2, 2, 2],
    [11, -2, 1, -4, 5, -3, 2, 2, 2],
]

test_answers = [7, -1, 3, 8, 14]

# Results
for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (max_consecutive_sum(test_input))
    print("\nOutput: " + str(test_output))
    print(test_output == test_answer)
