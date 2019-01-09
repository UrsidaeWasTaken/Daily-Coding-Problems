"""
Find the minimum number of coins required to make n cents. You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

# Solution
def minimum_coins(cents):
    total = 0
    coins_denominations = [100, 50, 25, 10, 5, 1]
    for coin in coins_denominations :
        total += cents // coin
        cents = cents % coin
    return total

# Custom Tests
test_inputs = [16, 1, 80, 99, 0, 128]
test_answers = [3, 1, 3, 8, 0, 5]

# Results
for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (minimum_coins(test_input))
    print("\nOutput: " + str(test_output))
    print(test_output == test_answer)