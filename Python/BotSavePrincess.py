# Problem
"""
Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. The goal is to reach the princess in as few moves as possible.

Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN. The grid size is always odd.

EXAMPLE:
---
-m-
p--

DOWN
LEFT
"""

# Solution
def displayPathtoPrincess(n,grid):
    path = ""
    if grid[0][0] == "p":
        path += "UP\nLEFT\n" * ((n-1)//2)
    elif grid[0][n-1] == "p":
        path += "UP\nRIGHT\n" * ((n-1)//2)
    elif grid[n-1][0] == "p":
        path += "DOWN\nLEFT\n" * ((n-1)//2)
    elif grid[n-1][n-1] == "p":
        path += "DOWN\nRIGHT\n" * ((n-1)//2)
    return path
            
# Explaination
"""
The princess is always located in one of the four corners of the grid, and you start in the middle. Therefore, we only ever have 4 possible paths. The path we go to depends on which corner the princess is in.
"""

# Results
test_inputs = [
    (3, ["---", "-m-", "p--"]),
    (5, ["p----", "-----", "--m--", "-----", "-----"]),
    (7, ["-------", "-------", "-------", "---m---", "-------", "-------", "------p"])
]
test_outputs = [
    "DOWN\nLEFT\n",
    "UP\nLEFT\nUP\nLEFT\n",
    "DOWN\nRIGHT\nDOWN\nRIGHT\nDOWN\nRIGHT\n"
]

for (test_input, test_output) in zip(test_inputs, test_outputs):
    result = displayPathtoPrincess(test_input[0],test_input[1])
    print(*test_input[1], sep='\n')
    print(f'\n{result}{result == test_output}\n')