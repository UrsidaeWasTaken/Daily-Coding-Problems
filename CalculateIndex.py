"""
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:
A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.

For example, if the citations of each paper are [4, 3, 0, 1, 5] then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
"""

# Solution
def calculate_h_index(citations):
    passed = citations.copy() # The h-index will always be an element in the array
    while passed:
        h_index = max(passed)
        occur = 0
        for citation in citations:
            occur += 1 if h_index <= citation else 0
            if occur == h_index:
                return h_index
        passed.remove(h_index)
    return 0

# Custom Tests
test_inputs = [[4, 3, 0, 1, 5], [100, 30, 2, 4], [0], [3, 1, 2, 57], [1, 60], [2, 2], [0, 5, 10, 15, 20]]
test_answers = [3, 2, 0, 2, 1, 2, 0]

# Results
for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = calculate_h_index(test_input)
    print("\nOutput: " + str(test_output))
    print(test_output == test_answer)
