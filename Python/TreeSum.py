"""
Given a root node, calculate the sum of all nodes in it's binary tree.

Example:
      2
    /   \
   4     6
  / \
 3   5

 Root: 2
 Nodes: 2, 3, 4, 5, 6
 Output: 20

Class Node {
    int data = data
    node left = None
    node right = None
}
"""

class Node():
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;

# Explaination
"""
We do a recursive depth-first traversal through the binary tree.
Keep calling tree_sum until we reach a leaf. A leaf has no branches (None), so it will return 0.
As it goes back up, it will return the next level's node data, which will sum its children's sum with its own to return to the next level until we reach the root.
The root will return the final sum.
"""

# Solution
def tree_sum(node):
    if node == None:
        return 0

    return int(node.data + tree_sum(node.left) + tree_sum(node.right))


# Test Cases
"""
      2
    /   \
   4     6
  / \
 3   5
"""
root1 = Node(2)
root1.left = Node(4)
root1.right = Node(6)
root1.left.left = Node(3)
root1.left.right = Node(5)

"""
      0
    /   \
   0     0
"""
root2 = Node(0)
root2.left = Node(0)
root2.right = Node(0)

"""
      39456
      /
   584234
    /  
   0   
  / 
 3  
"""
root3 = Node(39_456)
root3.left = Node(584_234)
root3.left.left = Node(0)
root3.left.left.left = Node(3)

"""
300 (Only root)
"""
root4 = Node(300)

test_inputs = [root1, root2, root3, root4]
test_answers = [20, 0, 623_693, 300]

# Test Solution
for i, answer in enumerate(test_answers):
    print(f'Test Case {i+1}:\n Solution Output: {tree_sum(test_inputs[i])}\n Answer: {test_answers[i]}\n')