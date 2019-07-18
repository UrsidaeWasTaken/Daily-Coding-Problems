"""
Given all the ratings data of existing phones in the market (ratings), create a program that analyses the data and suggests the best phone from the array of choices (phones).

The program must follow these rules in choosing the best phone:
    1) Choose the one with the highest rating average
    2) If there are many options from the above filter, choose the one which was rated by the maximum number of users
    3) If there are still many options, choose the one which appeared first in the 'phones' array

The 'ratings' array should be in the form of int[n][5] where the ratings of phones[i] are stored in ratings[i] and:
    ** ratings[i][0] = number of users who gave a rating of 5/5
    ** ratings[i][1] = number of users who gave a rating of 4/5
    ** ...ratings[i][4] = number of users who gave a rating of 1/5

NOTE: The rating average of a phone must be rounded to one decimal place before comparing them. For example: 3.8888 and 3.9112 should both be 3.9
"""

# Solution
def phone_rating(phones, ratings):
    highest = (0,0,0)
    for i in range(len(phones)):
        total = sum(ratings[i])
        if not total:
            continue
        for j in range(5):
            ratings[i][j] *= 5-j
        current = (round(sum(ratings[i])/total, 1), total, i)
        if (current[0] > highest[0]) or (current[0] == highest[0] and current[1] > highest[1]):
            highest = current
    return phones[highest[2]]

# Custom Tests
test_inputs_phones = [["Samsung", "Nokia", "Lenovo", "Asus", "iPhone", "Acer"], ["Samsung", "Nokia", "Lenovo", "Asus", "iPhone", "Acer"],
["Samsung", "Nokia", "Lenovo", "Asus"], ["iPhone", "Nokia", "Samsung"]]
test_inputs_ratings = [[[5,4,3,2,1], [25,44,32,200,10], [250,447,362,900,10], [470,4447,382,300,40], [600,900,850,50,22], [670,2744,1467,89,222]],
[[1,3,3,2,5], [1,2,3,4,5], [4,5,3,2,1], [4,1,3,3,5], [5,3,4,2,1], [5,2,3,4,5]],
[[1,2,6,3,4], [2,2,4,4,4], [1,2,4,4,5], [1,2,4,3,6]],
[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]]
test_answers = ["Asus", "Lenovo", "Samsung", "iPhone"]

# Results
for phones, ratings, expected_output in zip(test_inputs_phones, test_inputs_ratings, test_answers):
    solution_output = phone_rating(phones, ratings)
    print("\nOutput: " + str(solution_output))
    print(solution_output == expected_output)
