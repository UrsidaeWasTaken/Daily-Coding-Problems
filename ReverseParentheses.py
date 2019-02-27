"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

For example, given the string "foo(bar)baz", return "foorabbaz".
Also, given the string "foo(bar(baz))blim", return "foobazrabblim" because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""
import unittest

# Solution
def reverse_parentheses(string):
    stack = []
    for char in string:
        if char == ')':
            temp = ''
            while stack[-1] != '(':
                temp += stack.pop()
            stack.pop()
            for t in temp: stack.append(t)
        else: stack.append(char)         
    return ''.join(stack)

# Testing
class TestFileNaming(unittest.TestCase):
    def test_cipher(self):
        test_inputs = ["(bar)", "foo(bar)baz", "foo(bar)baz(blim)", "(abc)d(efg)", "foo(bar(baz))blim", "", "()"]
        test_answers = ["rab", "foorabbaz", "foorabbazmilb", "cbadgfe", "foobazrabblim", "", ""]

        for test_input, test_answer in zip(test_inputs, test_answers):
            self.assertEqual(reverse_parentheses(test_input), test_answer)

if __name__ == '__main__':
    unittest.main()