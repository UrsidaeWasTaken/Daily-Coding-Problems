"""
Given an integer 'product', find the smallest positive integer which digits multiply together to make that product. If there is no such integer, return -1 instead.
For example, given 12 as the product, the output should be 26.
"""

# Solution
def digits_product(product):
    if product == 1:
        return 1
    if not product:
        return 10
    
    res = []
    for factor in reversed(range(2, 10)):
        while product % factor == 0:
            product /= factor
            res.insert(0, str(factor))
    return -1 if product > 1 else int(''.join(res))

# Custom Tests
test_inputs = [12, 19, 450, 0, 13, 1, 0, 243]
test_answers = [26, -1, 2559, 10, -1, 1, 10, 399]

# Results
for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (digits_product(test_input))
    print("\nOutput: " + str(test_output))
    print(test_output == test_answer)