"""
Given a Roman numeral (String) between 1 and 3999, find the corresponding integer value.

For example, given 'IX' the output should be 9.

I     1
IV    4
V     5
IX    9 
X     10
XL    40
L     50
XC    90
C     100
CD    400
D     500
CM    900
M     1000
"""

# Solution
def roman_numerals(numerals):
    total = 0
    numerals += "."
    for i, numeral in enumerate(numerals):
        if numeral == 'M':
            if numerals[i-1] == 'C':
                total += 800
            else:
                total += 1000
        elif numeral == 'D':
            if numerals[i-1] == 'C':
                total += 300
            else:
                total += 500
        elif numeral == 'C':
            if numerals[i-1] == 'X':
                total += 80
            else:
                total += 100
        elif numeral == 'L':
            if numerals[i-1] == 'X':
                total += 30
            else:
                total += 50
        elif numeral == 'X':
            if numerals[i-1] == 'I':
                total += 8
            else:
                total += 10
        elif numeral == 'V':
            if numerals[i-1] == 'I':
                total += 3
            else:
                total += 5
        elif numeral == 'I':
            total += 1
    return total

# Custom Tests
test_inputs = ["MCMIV", "MMMCMXCVIII", "XXVII", "I", "IX", "CMXCIX"]
test_answers = [1904, 3998, 27, 1, 9, 999]

# Results
for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (roman_numerals(test_input))
    print("\nOutput: " + str(test_output))
    print(test_output == test_answer)