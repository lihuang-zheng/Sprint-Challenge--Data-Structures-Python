import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        removed_value = self.storage.remove_from_tail()

        self.size -= 1
        return removed_value

    def len(self):
        return self.size
