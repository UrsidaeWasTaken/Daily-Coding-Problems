"""
Given an array of time intervals (start, end) for classroom lectures (could overlap), the program should 
find the minimum number of rooms required.

For example, given the times [(30, 75), (0, 50), (60, 150)], the program should return 2.
"""

# Custom tests and answers
test_inputs = [[(30, 75), (0, 50), (60, 150)],
               [],
               [(0, 120), (10, 100), (50, 125), (20, 50)],
               [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (0, 50)]]
test_answers = [2, 0, 3, 2]


def time_interval(input_array):
    room_count = 0
    if input_array:
        input_array = sorted(input_array)
        room_count = 1
        last_overlap = -1
        for cur, nxt in zip(input_array, input_array[1:]):
            if cur[1] > nxt[0]:
                room_count += 1
                if nxt[0] >= last_overlap > -1:
                    room_count -= 1
                last_overlap = cur[1]
    return room_count


for test_input, test_answer in zip(test_inputs, test_answers):
    test_output = (time_interval(test_input))
    print("Output: " + str(test_output))
    print(test_output == test_answer)
