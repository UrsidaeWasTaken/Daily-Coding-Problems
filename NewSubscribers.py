"""
You are given an array of length 24, where each element represents the number of new subscribers during the corresponding hour. Implement a data structure that efficiently supports the following:
    • update(hour: int, value: int): Increment the element at index hour by value.
    • query(start: int, end: int): Retrieve the number of subscribers that have signed up between start and end (inclusive).

(note: You can assume that all values get cleared at the end of the day, and that you will not be asked for start and end values that wrap around midnight)
"""

# Solution
class NewSubscribers():
    def __init__(self, subscribers=None):
        if not subscribers or len(subscribers) != 24:
            subscribers = [0]*24 #Automatically fills array if empty
        
        self.subscribers = subscribers

    def update(self, hour, value):
        hour -= 1
        self.subscribers[hour] += value

    def query(self, start, end):
        start -= 1
        return self.subscribers[start:end]
    
# Tests & Results
example1 = NewSubscribers()
print("Example 1: {}".format(example1.subscribers))

example2 = NewSubscribers(list(range(1, 48, 2)))
print("\nExample 2: {}".format(example2.subscribers))
example2.update(5, 13)
print("\nNew subscribers from 2-10 hours in Example 2: {}".format(example2.query(2, 10)))