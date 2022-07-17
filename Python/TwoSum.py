# Problem
"""
Given an array of nums (int) and a target (int), return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. The array will always have at least two integers.
Return in accending order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# Explaination
"""
First, create a dictionary.
Then, for each number in the array, find its complement number (compliment = target - num).

Check if the compliment number is in the dictionary.

If it is, return the current and compliment's number indices.

Else, add a key-value pair for the current number and its index (key: Current number, value: Current index).
If we find its compliment number later in the array, we can quickly access it.
"""

# Solution
def two_sum(nums, target):
    # Dictionary to store each number and index we've passed.
    compliments = {}
    
    for i, num in enumerate(nums):
        # Get compliment number (target - num)
        compliment = target - num

        # If compliment number in compliments dictionary, return current and compliment's number indices 
        if compliment in compliments:
            return [compliments[compliment], i]
        # Else, add number and index to compliments
        else:
            compliments[num] = i

# Test Cases
test_inputs = [([2,7,11,15], 9), ([12,14,15,10,13,3], 13), ([70,1,0], 70), ([1,1],2)]
test_answers = [[0,1], [3,5], [0,2], [0,1]]

for i, case in enumerate(test_inputs):
    solution_answer = two_sum(case[0], case[1])
    print(f'Test Case {i+1}:\n Solution Output: {solution_answer}\n Answer: {test_answers[i]}\n')