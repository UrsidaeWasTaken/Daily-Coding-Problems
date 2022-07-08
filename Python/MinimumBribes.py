# Problem
"""
People are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to N.
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Return the number of bribes, or, if anyone has bribed more than two people, return -1.

Input:
    int q[n]: the positions of the people after all bribes.

Example:
    q = [1,2,3,5,4,6,7,8]
    If person 5 bribes person 4, the queue will look like this: [1,2,3,5,4,6,7,8]. Only 1 bribe is required. Return 1.

    q = [4,1,2,3]
    Person 4 had to 3 bribe people to get to the current position. No person can bribe more than two people. Return -1.
"""

# Explaination
"""
Since any person can't bribe more than two people, we can create a list of valid values a person in a given position move to (starting from the first position).

If the person matches valid_values[0], the person made no bribes.
If the person matches valid_values[1], the person made 1 bribe to reach that spot. We add 1 to the total bribes.
If the person matches valid_values[2], the person made 2 bribes to reach that spot. We add 2 to the total bribes.
Regardless, we must pop the position it matches as there can only be one match per person.
If the person matches no valid values, return -1.
"""

# Solution
def minimumBribes(q):
    # List of valid positions the person can be
    valid = [1,2,3]
    # Total bribes
    bribes = 0
    
    # Loop through each person in the queue
    for person in q:
        # Append the next position in queue to valid
        valid.append(valid[-1]+1)

        # If person == valid[0], the person made no bribes. Pop Valid[0].
        if person == valid[0]:
            valid.pop(0)
        # If person matches valid[1], the person made 1 bribe. Pop Valid[1] & increment bribes by 1.
        elif person == valid[1]:
            valid.pop(1)
            bribes += 1
        # If person matches valid[2], the person made 2 bribes. Pop Valid[2] & increment bribes by 2.
        elif person == valid[2]:
            valid.pop(2)
            bribes += 2
        # Else the person made more than 2 bribes. Return -1
        else:
            return -1
                
    return bribes

# Test Cases
test_inputs = [
    [2,1,5,3,4],
    [2,5,1,3,4],
    [5,1,2,3,7,8,6,4],
    [1,2,5,3,7,8,6,4],
    [1],
    [2,1],
    [3,2,1],
    [4,1,2,3],
    [1,2,3,5,4,6,7]
]

actual_answers = [3,-1,-1,7,0,1,3,-1,1]

for i in range(len(actual_answers)):
    solution_answer = minimumBribes(test_inputs[i])
    print(f'Test Case {i+1}:\n Solution Output: {solution_answer}\n Answer: {actual_answers[i]}\n')
