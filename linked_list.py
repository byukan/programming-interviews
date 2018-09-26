"""
    @file linked_list.py
    @brief LinkedList class
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # def get_position(self, p):
    #     """Get an element from a particular position.
    #     Assume the first position is "1".
    #     Return "None" if position is not in the list.
    #     :param p: position to get element
    #     :return: element at certain position
    #     """
    #     if self.head is None:
    #         return 0
    #     else:
    #         current = self.head
    #         i = 0
    #         while i < p and current.next:


    # front insert
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # back insert
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    @staticmethod
    def display(head):
        current = head
        while current.next is not None:
            print(current.data)


# my_list = LinkedList()
# head = None
# head = my_list.append(4)

# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.data)
# Should also print 3
print(ll.get_position(3).data)
