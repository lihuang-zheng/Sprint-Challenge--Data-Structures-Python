class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class CircularLinkedList:
    def __init__(self, length):
        newest = Node()
        self.entry = newest
        self.print_start = newest

        for i in range(length - 1):
            newest.next = Node()
            newest = newest.next

        newest.next = self.entry

    def __str__(self):
        current_node = self.print_start
        string_representation = str(current_node.value)

        while current_node.next is not self.print_start:
            current_node = current_node.next

            if current_node.value:
                string_representation += " >>> " + str(current_node.value)

        string_representation += " >>> " + str(self.print_start)

        return string_representation

    def get_array_representation(self):
        current_node = self.print_start
        array_representation = []

        if current_node.value:
            array_representation.append(current_node.value)

        while current_node.next is not self.print_start:
            current_node = current_node.next
            if current_node.value:
                array_representation.append(current_node.value)

        return array_representation


class RingBufferAsCircularLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = CircularLinkedList(capacity)

    def __str__(self):
        return str(self.storage)

    def append(self, item):
        self.storage.entry.value = item
        self.storage.entry = self.storage.entry.next

    def get(self):
        return self.storage.get_array_representation()


class RingBufferAsArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
        self.entry_index = 0

    def __str__(self):
        return " >>> ".join(self.storage)

    def append(self, item):
        self.storage[self.entry_index] = item
        self.entry_index = (self.entry_index + 1) % self.capacity

    def get(self):
        return [value for value in self.storage if value]


class RingBuffer(RingBufferAsArray):
    def __init__(self, capacity):
        super().__init__(capacity)
