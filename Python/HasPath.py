# Problem
"""
Given a Directed Graph (via adjacency list) and two vertices, check whether there is a path from the first given vertex to second.
"""
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
    'g': ['h'],
    'h': []
}

# Explaination
"""
Either Breadth First Search (BFS) or Depth First Search (DFS) can be used to find path between two vertices. Take the first vertex as the source.
If the second vertex is found in our traversal, then return true else return false.

BFS can be done either iteratively or recursively.
"""

# Solution - Iterative BFS method
from collections import deque

def has_path(graph, source, dest):
    if source == dest:
        return True

    queue = deque(source)
    while(queue):
        # Get current node
        current = queue.popleft()
        # Return if current node is destination
        if current == dest:
            return True

        # Else, add current node's neighbours to queue
        for neighbour in graph[current]:
            queue.append(neighbour)

    return False

# Solution - Recursive DFS method
def has_path_recursive(graph, source, dest):
    if source == dest:
        return True

    for neighbor in graph[source]:
        if has_path_recursive(graph, neighbor, dest) == True:
            return True
    
    return False

# Test cases
test_source = ['a', 'a', 'e', 'b', 'g', 'h', 'a']
test_dest = ['f', 'g', 'c', 'd', 'h', 'h', 'z']
test_answers = [True, False, False, True, True, True, False]

for i in range(len(test_answers)):
    print("Iterative Method")
    solution_answer = has_path(graph, test_source[i], test_dest[i])
    print(f'Test Case {i+1}:\n Solution Output: {solution_answer}\n Answer: {test_answers[i]}\n')

for i in range(len(test_answers)):
    print("Recusrive Method")
    solution_answer = has_path_recursive(graph, test_source[i], test_dest[i])
    print(f'Test Case {i+1}:\n Solution Output: {solution_answer}\n Answer: {test_answers[i]}\n')