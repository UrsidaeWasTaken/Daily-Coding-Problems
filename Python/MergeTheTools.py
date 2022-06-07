# PROBLEM
"""
Consider the following:
A string, s, of length n where s = c[0], c[1]... c[n-1].
An integer, k, where k is a factor of n.

We can split s into n/k substrings where each substring, t[i], consists of a contiguous block of
k characters, such that:
    • The characters in t[i] are a subsequence of the characters in s.
    • Any repeat occurrence of a character is removed from the string such that each character in t[i]
    occurs exactly once.
Given s and k, return a list of n/k subsequences where each subsequence denotes string t[i].

EXAMPLE:
s = 'AAABCADDE'
k = 3

There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'.
The first substring is all 'A' characters, so t[1] = 'A'.
The second substring has all distinct characters, so t[2] = 'BCA'.
The third substring has 2 different characters, so t[3] = 'DE'.

Note that a subsequence maintains the original order of characters encountered.
"""

# EXPLAINATION
"""
To simplify this problem, split a string into groups of "k" (k being a number given to us),
but each group cannot have duplicate characters within them.

To solve this, we will create a new empty string, which we will add each character from s into if it's NOT already in the new string.
However, every k characters, we will move the current string into the results list and start a new string.

Return the 'Results' list.
"""

# SOLUTION
def solution(s, k):
    results = []
    curr_string = ""
    count = 0

    for char in s:
        count += 1
        if char not in curr_string:
            curr_string += char
        if count == k:
            results.append(curr_string)
            curr_string = ""
            count = 0
    
    return results

# TEST CASES
test_inputs = [
    ("AABCAAADA", 3),
    ("COAAAOAOSMMSDDMKKLLL", 4),
    ("AAAA", 4),
    ("QWERTY", 3),
    ("ABCDEFGHGFEDCBA", 5),
    ("DOWTJAHBJKRXASYLDEQQXLQBFHLZXIKAZHVIJROAZKLUNCQQCLNZNLCSYSCOODKMXRBYKPBLZMGMQYDSMSRZDVRDPUSDZERYVSWFIZRHNZUDZZVLROKWJEABGZIBDLVHPIUXMUPZHVGISAJLRRUTCTARPVIYKGKCEXIYTXYDSGLLGUWAOSTSMTMDPUBBCLDGKLFELFHDNUQUPPUFHPXTLLWCFZDIKJQXUXDHCKLQGDMVSIACXAVKLUMTTQBGBRFXPIFTSSJAVXWQFYSFAPPMLCFFUINVBSUSAZMURXUNVSFCTXHTOXFABMHVUWSYOMQQOCMFCGUXBZZUYJNNGV", 1)
]

test_answers = [
    ['AB', 'CA', 'AD'],
    ['COA', 'AO', 'SM', 'DMK', 'KL'],
    ['A'],
    ['QWE', 'RTY'],
    ['ABCDE', 'FGH', 'EDCBA'],
    ['D', 'O', 'W', 'T', 'J', 'A', 'H', 'B', 'J', 'K', 'R', 'X', 'A', 'S', 'Y', 'L', 'D', 'E', 'Q', 'Q', 'X', 'L', 'Q', 'B', 'F', 'H', 'L', 'Z', 'X', 'I', 'K', 'A', 'Z', 'H', 'V', 'I', 'J', 'R', 'O', 'A', 'Z', 'K', 'L', 'U', 'N', 'C', 'Q', 'Q', 'C', 'L', 'N', 'Z', 'N', 'L', 'C', 'S', 'Y', 'S', 'C', 'O', 'O', 'D', 'K', 'M', 'X', 'R', 'B', 'Y', 'K', 'P', 'B', 'L', 'Z', 'M', 'G', 'M', 'Q', 'Y', 'D', 'S', 'M', 'S', 'R', 'Z', 'D', 'V', 'R', 'D', 'P', 'U', 'S', 'D', 'Z', 'E', 'R', 'Y', 'V', 'S', 'W', 'F', 'I', 'Z', 'R', 'H', 'N', 'Z', 'U', 'D', 'Z', 'Z', 'V', 'L', 'R', 'O', 'K', 'W', 'J', 'E', 'A', 'B', 'G', 'Z', 'I', 'B', 'D', 'L', 'V', 'H', 'P', 'I', 'U', 'X', 'M', 'U', 'P', 'Z', 'H', 'V', 'G', 'I', 'S', 'A', 'J', 'L', 'R', 'R', 'U', 'T', 'C', 'T', 'A', 'R', 'P', 'V', 'I', 'Y', 'K', 'G', 'K', 'C', 'E', 'X', 'I', 'Y', 'T', 'X', 'Y', 'D', 'S', 'G', 'L', 'L', 'G', 'U', 'W', 'A', 'O', 'S', 'T', 'S', 'M', 'T', 'M', 'D', 'P', 'U', 'B', 'B', 'C', 'L', 'D', 'G', 'K', 'L', 'F', 'E', 'L', 'F', 'H', 'D', 'N', 'U', 'Q', 'U', 'P', 'P', 'U', 'F', 'H', 'P', 'X', 'T', 'L', 'L', 'W', 'C', 'F', 'Z', 'D', 'I', 'K', 'J', 'Q', 'X', 'U', 'X', 'D', 'H', 'C', 'K', 'L', 'Q', 'G', 'D', 'M', 'V', 'S', 'I', 'A', 'C', 'X', 'A', 'V', 'K', 'L', 'U', 'M', 'T', 'T', 'Q', 'B', 'G', 'B', 'R', 'F', 'X', 'P', 'I', 'F', 'T', 'S', 'S', 'J', 'A', 'V', 'X', 'W', 'Q', 'F', 'Y', 'S', 'F', 'A', 'P', 'P', 'M', 'L', 'C', 'F', 'F', 'U', 'I', 'N', 'V', 'B', 'S', 'U', 'S', 'A', 'Z', 'M', 'U', 'R', 'X', 'U', 'N', 'V', 'S', 'F', 'C', 'T', 'X', 'H', 'T', 'O', 'X', 'F', 'A', 'B', 'M', 'H', 'V', 'U', 'W', 'S', 'Y', 'O', 'M', 'Q', 'Q', 'O', 'C', 'M', 'F', 'C', 'G', 'U', 'X', 'B', 'Z', 'Z', 'U', 'Y', 'J', 'N', 'N', 'G', 'V']
]

# RESULTS
for (test_input, test_answer) in zip(test_inputs, test_answers):
    test_output = (solution(test_input[0], test_input[1]))
    print("\nOutput: " + str(test_output))
    print("Expected: " + str(test_answer))
    print(test_output == test_answer)