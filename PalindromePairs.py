"""
Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)]
"""

# Solution
def palindrome_pairs(words):
    res = [] # Output list
    for i, word in enumerate(words):
        for j in range(i+1, len(words)): # Looping the whole list is redundant
            if word+words[j] == (word+words[j])[::-1]:
                res.append((i, j))
            if (words[j]+word)[::-1] == words[j]+word:
                res.append((j, i))
    return res

# Custom Tests
test_inputs = [["code", "edoc", "da", "d"], ["bat","tab","cat"], ["abcd","dcba","lls","s","sssll"]]
test_answers = [[(0, 1), (1, 0), (2, 3)], [(0, 1),(1, 0)], [(0, 1), (1, 0), (3, 2), (2, 4)]]

# Results
for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (palindrome_pairs(test_input))
    print("\nOutput: " + str(test_output))
    print(test_output == test_answer)