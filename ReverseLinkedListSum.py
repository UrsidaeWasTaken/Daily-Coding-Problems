"""
If a linked list represents a number, each node in the linked list represents a digit of the number. The linked list is also in reversed order.

For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5 is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.
For example, given the linked list 9 -> 9 and 5 -> 2 return 124 (99 + 25) as: 4 -> 2 -> 1
"""

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        display = []
        cur_node = self.head
        while cur_node:
            display.append(cur_node.data)
            cur_node = cur_node.next
        return display

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
    
    # Converts linked list to reversed integer
    def linkedlist_to_int(self):
        num = []
        cur_node = self.head
        while cur_node:
            num.append(str(cur_node.data))
            cur_node = cur_node.next
        return int(''.join(reversed(num)))

# Sum of 2 reversed linked lists, returns result in same reversed format
def reverse_sum(num1, num2):
    result = LinkedList()
    listsum = num1.linkedlist_to_int() + num2.linkedlist_to_int()
    for num in reversed(str(listsum)):
        result.append(int(num))
    return result.display()

# Linked Lists Examples
llist1 = LinkedList()
llist2 = LinkedList()
llist3 = LinkedList()

llist1.append(3)
llist1.append(7)
llist1.append(8)
llist1.append(5)

llist2.append(6)
llist2.append(3)
llist2.append(3)
llist2.append(2)

llist3.append(5)
llist3.append(0)
llist3.append(2)
llist3.append(8)

# Custom Tests
print("Linked List 1: " + str(llist1.display()))
print("Linked List 2: " + str(llist2.display()))
print("Linked List Result: " + str(reverse_sum(llist1, llist2)))

print("\nLinked List 1: " + str(llist1.display()))
print("Linked List 3: " + str(llist3.display()))
print("Linked List Result: " + str(reverse_sum(llist1, llist3)))

print("\nLinked List 2: " + str(llist2.display()))
print("Linked List 3: " + str(llist3.display()))
print("Linked List Result: " + str(reverse_sum(llist2, llist3)))
