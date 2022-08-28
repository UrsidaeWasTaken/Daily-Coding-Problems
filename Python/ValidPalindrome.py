# Problem
"""
Given a Phrase (string), return if it is a palindrome (bool).
Palindrome is a phrase that reads the same forward and backward.
"""

# Notes & Working-Outs
"""
Constraints
1 <= Phrase Length <= 10^5

Return Bool:
True if Palindrome
False if not Palindrome

Examples:
"race a car" <- False
"Race car." <- True, spaces and punctuation are ignored. Case-insensitive.

Only Alphanumeric should be acknowledged. (Numebers and Letters)

1. Given Phrase (String)
2. Create empty string variable for phrase excluding non-alphanumeric characters.
3. Loop through each character in phrase.
4. Check if character is alphanumeric (letter or number).
5. If character is alphanumeri, add to empty string variable.
    Else, ignore.
6. Check if new phrase variable reads the same forwards and backwards.
7. If it reads the same forwards and backwards, return True.
    Else, return False.
"""

# Solution
def is_palindrome(phrase: str) -> bool:
    # Phrase with only alphanumeric characters
    palindrome_phrase: str = ""

    # Ignore all non-alphanumeric characters in phrase
    for char in phrase:
        if char.isalpha():
            palindrome_phrase += char.lower() # Case-insensitive

    # Check if phrase is the same reversed
    return palindrome_phrase == palindrome_phrase[::-1]

# Testing
test_inputs = ["A man, a plan, a canal: Panama", " ", "race a car", ".O.", "NEVER odd or EVEN!", "Do Geese see Gods?", "By"]
test_answers = [True, True, False, True, True, False, False]

for i, case in enumerate(test_inputs):
    solution_answer = is_palindrome(case)
    print(f'Test Case {i+1}:\n Solution Answer: {solution_answer}\n Actual Answer: {test_answers[i]}\n')