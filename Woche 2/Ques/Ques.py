class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):

        neue_node = Node(data)
        if self.head is None:
            self.head = neue_node
            self.tail = neue_node

        else:
            self.tail.next = neue_node
            self.tail = neue_node

        self.size += 1

    def dequeue(self):
        if self.head is None:
            print("Queue ist leer!")
            return None

        wert = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None

            return wert

    def iter(self):
        current = self.head

        while current:
            value = current.data
            current = current.next
            yield value

def print_words():
    print(f"the list contains the following {queue.size} items:")
    for queues in queue.iter():
        print(f"\t{queues}")
    print("\n")

queue = Queue()

queue.enqueue("Burkay")
queue.enqueue("Dominique")
queue.enqueue("Louis")

print_words()


print(queue.dequeue())   
print(queue.dequeue())
print_words()
