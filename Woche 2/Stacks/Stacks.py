class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        #neues Objekt
        neues_node = Node(data)

        neues_node.next = self.top
        self.top = neues_node

        self.size += 1

    def pop(self):
       if self.top is None:
           print("Die Liste ist Leer")
           return None

       else:
           wert = self.top.data
           self.top = self.top.next
           self.size -= 1
           return wert

    def peek(self):
        if self.top is None:
            print("Der Node ist leer")
            return None

        else:
            return self.top.data


stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")
# top → [C]──►[B]──►[A]

print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.size)



