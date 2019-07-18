"""
For an integer k rearrange all the elements of the given array in such way, that:
    • All elements that are less than k are placed before elements that are not less than k;
    • All elements that are less than k remain in the same order with respect to each other;
    • All elements that are not less than k remain in the same order with respect to each other.

For example, if k = 5 and elements = [1, 3, 5, 7, 6, 4, 2], the output should be [1, 3, 4, 2, 5, 7, 6].
"""

# Solution
def split_by_value(k, nums):
    return [*filter(lambda num: num < k, nums), *filter(lambda num: num >= k, nums)]

# Custom Tests
test_inputs = [
    [5, [1, 3, 5, 7, 6, 4, 2]], 
    [0, [5, 2, 7, 3, 2]], 
    [10, [10, 2, 3, 5, 6, 0]]
    ]
test_answers = [
    [1, 3, 4, 2, 5, 7, 6], 
    [5, 2, 7, 3, 2], 
    [2, 3, 5, 6, 0, 10]
    ]

# Results
for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (split_by_value(test_input[0], test_input[1]))
    print("\nOutput: " + str(test_output))
    print(test_output == test_answer)
