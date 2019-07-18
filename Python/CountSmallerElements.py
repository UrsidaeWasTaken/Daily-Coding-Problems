"""
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array. 
For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0]
"""

# Custom tests
test_inputs = [[3, 4, 9, 6, 1], [11], [5, 1, 5, 1, 5, 1]]

# Custom answers
test_answers = [[1, 1, 2, 1, 0], [0], [3, 0, 2, 0, 1, 0]]

def count_smaller_elements(nums):
    result = []
    if len(nums) > 1:
        for i, num1 in enumerate(nums[:-1]):
            count = 0
            for num2 in nums[i:]:
                if num2 < num1:
                    count += 1
            result.append(count)
    result.append(0)
    return result

for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (count_smaller_elements(test_input))
    print("Output: " + str(test_output))
    print(test_output == test_answer)
