"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names,
the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such
that the obtained name is not used yet. Return an array of names that will be given to the files.

For example, given the array ["doc", "doc", "image", "doc(1)", "doc"], return ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
"""
import unittest

# Solution
def file_naming(files):
    for i in range(len(files)):
        if files[i] in files[:i]:
            k = 1
            while files[i]+"(%s)" % k in files[:i]:
                k += 1
            files[i] += "(%s)" % k
    return files

# Testing
class TestFileNaming(unittest.TestCase):
    def test_file_naming(self):
        test_inputs = [
            ["doc", "doc", "image", "doc(1)", "doc"],
            ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]
        ]
        test_answers = [
            ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"],
            ["a(1)", "a(6)", "a", "a(2)", "a(3)", "a(4)", "a(5)", "a(7)", "a(8)", "a(9)", "a(10)", "a(11)"],
            ["dd", "dd(1)", "dd(2)", "dd(3)", "dd(1)(1)", "dd(1)(2)", "dd(1)(1)(1)", "dd(4)", "dd(1)(3)"]
        ]

        for test_input, test_answer in zip(test_inputs, test_answers):
            self.assertEqual(file_naming(test_input), test_answer)

if __name__ == '__main__':
    unittest.main()
