class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circles:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        neuer_node = Node(data)

        if self.head is None:
            self.head = neuer_node
            self.tail = neuer_node

        else:
            self.tail.next = neuer_node
            self.tail = neuer_node
            self.tail.next = self.head

        self.size += 1

    def iter(self):

        current = self.head

        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break

liste = Circles()
liste.append("A")
liste.append("B")
liste.append("C")

for item in liste.iter():
    print(item)