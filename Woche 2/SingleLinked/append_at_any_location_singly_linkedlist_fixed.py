class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        # Encapsulate the data in a Node
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def append_at_a_location(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 0 # FIX: start at 0 since we want a zero-offset list
        while current:
            if index == 0: # FIX: use index, not count to determine whether we insert at the start
                node.next = current
                self.head = node
                return
            elif index == count: # FIX: compare index to count, not to itself
                node.next = current
                prev.next = node
                return
            count += 1
            prev = current
            current = current.next
        if count < index:
            print("The list has less number of elements")





words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current = current.next
print('---') # added for clarity in output


words.append_at_a_location('new', 2)
print('---') # added for clarity in output
current = words.head
while current:
    print(current.data)
    current = current.next