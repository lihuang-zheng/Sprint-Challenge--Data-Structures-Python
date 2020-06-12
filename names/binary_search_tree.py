import sys
from d_queue import Queue
from d_stack import Stack
from collections import deque


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            if self.left is None:
                return False
            return self.left.contains(target)

    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def iterative_for_each(self, cb):
        stack = []

        stack.append(self)

        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)

            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_first_iterative_for_each(self, cb):
        q = deque()
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)

    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(node)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(node)

    def bft_print(self, node):
        self.breadth_first_iterative_for_each(lambda value: print(value))

    def dft_print(self, node):
        self.iterative_for_each(lambda value: print(value))

    def pre_order_dft(self, node):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_dft(node)
        if self.right is not None:
            self.right.pre_order_dft(node)

    def post_order_dft(self, node):
        if self.left is not None:
            self.left.post_order_dft(node)
        if self.right is not None:
            self.right.post_order_dft(node)
        print(self.value)
