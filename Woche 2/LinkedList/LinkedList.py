# Agarwal and Baka, "Hands-On Data Structures and Algorithms with Python" 3rd Edition
class Node:
    """ A singly-linked node. """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """ A singly-linked list. """

    def __init__(self):
        """ Create an empty list. """
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        """ Append an item to the end of the list. """
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def iter(self):
        """ Iterate through all items in the list. """
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        """ Delete a node from the list. """
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        """ Search through the list.
        Return True if data is found, otherwise False. """
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        """ Clear the entire list. """
        self.tail = None
        self.head = None


if __name__ == "__main__":

    def print_words():
        print(f"the list contains the following {words.size} items:")
        for word in words.iter():
            print(f"\t{word}")
        print("\n")


    words = SinglyLinkedList()

    # append
    print("append items to the list")
    words.append("foo")
    words.append("bar")
    words.append("bim")
    words.append("baz")
    words.append("quux")
    print_words()

    # delete
    print("delete items from the list")
    words.delete("bim")
    print_words()
    words.delete("not in list")
    print_words()

    # search
    print("search item in the list")
    for search_word in ["baz", "foo", "other"]:
        result = words.search(search_word)
        print(f"\tsearching for {search_word} returned {result}")