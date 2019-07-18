"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence would be [1, 2, 3, 4] and should return 4.
"""

# Custom Tests
test_inputs = [
    [100, 4, 200, 1, 3, 2],
    [20, 1, 19, 3, 2, 40, 18, 17],
    [1, 1, 1, 1],
    [2, 0, 12, -1, 2, 1, 30, 3],
    [1, 3, 5, 7, 9, 11],
]

test_answers = [4, 4, 1, 5, 1]

# Solution
def longestConsecutive(nums):
    longest = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            cur_num = num
            cur_length = 1

            while cur_num + 1 in num_set:
                cur_num += 1
                cur_length += 1

            longest = max(longest, cur_length)

    return longest

# Results
for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (longestConsecutive(test_input))
    print("\nOutput: " + str(test_output))
    print(test_output == test_answer)
