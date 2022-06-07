# Problem
"""
Given a string, return its encoding defined as follows:

    First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
        for example, "aabbbc" is divided into ["aa", "bbb", "c"]
    Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
        for example, substring "bbb" is replaced by "3b"
    Finally, all the new strings are concatenated together in the same order and a new string is returned.

EXAMPLE:
"aabbbc" should output "2a3bc".
"""

# Explaination
"""
We loop through the string once. Counting every subsequent character that is identical until one isn't.
If the count is greater than 1 we should append the character with the count. Else, just the character.
Countinue this until the loop has reached the end and we'll get our solution.
"""

# Solution 
def solution(s):
    s += "."
    char_count = 0
    identical_char = []
    prev = s[0]
    for i, char in enumerate(s):
        # Increment the count by 1 if it's the same character as the previous.
        if prev == char:
            char_count += 1
        else:
            # If the count is bigger than 1, include the count when appending. Else, just the character.
            if char_count > 1:
                substring = "%s%s" % (char_count, prev)
                identical_char.append(substring)
            else:
                identical_char.append(prev)
            char_count = 1
        prev = char # Current now becomes previous character.
    return ''.join(identical_char)

# Custom Tests
test_inputs = ["aabbbc", "abbcabb", "abcd", "zzzz", "wwwwwwwawwwwwww", "ccccccccccccccc", "qwertyuioplkjhg", "ssiiggkooo", "adfaaa", "bbjaadlkjdl"]
test_answers = ["2a3bc", "a2bca2b", "abcd", "4z", "7wa7w", "15c", "qwertyuioplkjhg", "2s2i2gk3o", "adf3a", "2bj2adlkjdl"]

# Results
for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (solution(test_input))
    print("\nOutput: " + str(test_output))
    print("Expected: " + str(test_answer))
    print(test_output == test_answer)