# This file contains the source code for the implementation of 
# binary search tree.

# class BinarySearchTree:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # intailize the tree
    def binary_search_tree(self, data):
        self.insert(data)
            

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def delete(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.delete(data)
            elif data > self.data:
                if self.right:
                    self.right.delete(data)
            else:
                if self.left and self.right:
                    self.data = self.right.findMin()
                    self.right.delete(self.data)
                elif self.left:
                    self.data = self.left.data
                    self.left = None
                elif self.right:
                    self.data = self.right.data
                    self.right = None
                else:
                    self.data = None

    def find(self, data):
        if data < self.data:
            if self.left is None:
                return False
            return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return False
            return self.right.find(data)
        else:
            return True

    def preorder(self):
        if self.data:
            print(str(self.data), end = ' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self.data:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.data), end = ' ')

    def inorder(self):
        if self.data:
            if self.left:
                self.left.inorder()
            print(str(self.data), end = ' ')
            if self.right:
                self.right.inorder()

    def height(self):
        if self.data:
            if self.left and self.right:
                return 1 + max(self.left.height(), self.right.height())
            elif self.left:
                return 1 + self.left.height()
            elif self.right:
                return 1 + self.right.height()
            else:
                return 1
        else:
            return 0

    def size(self):
        if self.data:
            if self.left and self.right:
                return 1 + self.left.size() + self.right.size()
            elif self.left:
                return 1 + self.left.size()
            elif self.right:
                return 1 + self.right.size()
            else:
                return 1
        else:
            return 0

    def leaves(self):
        if self.data:
            if self.left and self.right:
                return self.left.leaves() + self.right.leaves()
            elif self.left:
                return self.left.leaves()
            elif self.right:
                return self.right.leaves()
            else:
                return 1
        else:
            return 0

    def findMin(self):
        if self.left:
            return self.left.findMin()
        else:
            return self.data

    def findMax(self):
        if self.right:
            return self.right.findMax()
        else:
            return self.data

    def traverse(self):
        if self.data:
            yield self.data
            if self.left:
                yield from self.left.traverse()
            if self.right:
                yield from self.right.traverse()

    def traverse_level(self):
        if self.data:
            queue = [self]
            while queue:
                node = queue.pop(0)
                yield node.data
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def traverse_level_reverse(self):
        if self.data:
            queue = [self]
            while queue:
                node = queue.pop()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                yield node.data

    def traverse_level_reverse_recursive(self):
        if self.data:
            yield self.data
            if self.right:
                yield from self.right.traverse_level_reverse_recursive()
            if self.left:
                yield from self.left.traverse_level_reverse_recursive()

# end of class BinarySearchTree

