# Problem
"""
This is an additional problem I made to the original MarioSavePrincess to make it harder, removing some of the limitations.

Princess Peach is trapped in a square grid. Mario can move one step at a time in any of the four directions. The goal is to get Mario to the princess in as few moves as possible.

Print out the moves Mario will need to take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.
"""

def displayPathtoPrincess(n,grid):
    path = ""

    # Retrieve Mario and Peach's location
    for i, row in enumerate(grid):
        if "p" in row:
            peach = (i,row.index("p"))
        if "m" in row:
            mario = (i,row.index("m"))
    
    # Check if Mario is above or below peach (or neither)
    if mario[0] > peach[0]:
        path += "UP\n" * abs(mario[0]-peach[0])
    else:
        path += "DOWN\n" * abs(mario[0]-peach[0])

    # Check if Mario is left or right of peach (or neither)
    if mario[1] > peach[1]:
        path += "LEFT\n" * abs(mario[1]-peach[1])
    else:
        path += "RIGHT\n" * abs(mario[1]-peach[1])
    
    return path

# Explaination
"""
We first need to know where Mario and Peach are located on the grid, then we want to compare Mario's location to Peach's location. Once we know Mario's distance from Peach, we use the abs function to create a path.
"""

# Results
test_inputs = [
    (3, ["p-m", "---", "---"]),
    (5, ["--p--", "-----", "-----", "-----", "----m"]),
    (7, ["-------", "-------", "-------", "---m---", "-------", "-------", "------p"]),
    (5, ["-----", "-p---", "-----", "-m---", "-----"]),
    (6, ["------", "------", "m-----", "-----p", "------", "------"])
]
test_outputs = [
    "LEFT\nLEFT\n",
    "UP\nUP\nUP\nUP\nLEFT\nLEFT\n",
    "DOWN\nDOWN\nDOWN\nRIGHT\nRIGHT\nRIGHT\n",
    "UP\nUP\n",
    "DOWN\nRIGHT\nRIGHT\nRIGHT\nRIGHT\nRIGHT\n"
]

for (test_input, test_output) in zip(test_inputs, test_outputs):
    result = displayPathtoPrincess(test_input[0],test_input[1])
    print(*test_input[1], sep='\n')
    print(f'\n{result}{result == test_output}\n')