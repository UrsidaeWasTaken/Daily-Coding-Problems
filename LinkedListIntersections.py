"""
Given two singly linked lists that intersect at some point, find the first intersecting node.
The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
"""

class Node(object):
    def __init__(self, data):
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

    def length(self, list=None):
        cur_node = self.head
        if list:
            cur_node = list
        length = 0
        while cur_node:
            cur_node = cur_node.next
            length += 1
        return length

def intersect(list_a, list_b):
    head_a, head_b = list_a.head, list_b.head
    cur_a, cur_b = head_a, head_b
    while cur_a.data is not cur_b.data:
        if not cur_a.next or not cur_b.next:
            return None
        cur_a = cur_a.next
        cur_b = cur_b.next
    return cur_a.data


llist1 = LinkedList()
llist2 = LinkedList()
llist3 = LinkedList()
llist4 = LinkedList()

llist1.append(3)
llist1.append(7)
llist1.append(8)
llist1.append(10)

llist2.append(99)
llist2.append(1)
llist2.append(8)
llist2.append(10)

llist3.append(10)
llist3.append(7)
llist3.append(20)
llist3.append(9.5)

llist4.append(6)
llist4.append(1)
llist4.append(11)
llist4.append(9.5)

# Custom Tests
print("List 1: " + str(llist1.display()))
print("List 2: " + str(llist2.display()))
print("Intersection: " + str(intersect(llist2, llist1)))

print("\nList 3: " + str(llist3.display()))
print("List 4: " + str(llist4.display()))
print("Intersection: " + str(intersect(llist3, llist4)))

print("\nList 1: " + str(llist1.display()))
print("List 3: " + str(llist3.display()))
print("Intersection: " + str(intersect(llist1, llist3)))

print("\nList 1: " + str(llist1.display()))
print("List 4: " + str(llist4.display()))
print("Intersection: " + str(intersect(llist1, llist4)))
