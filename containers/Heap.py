from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        left = True
        right = True
        if node is None:
            return True

        x_left = Heap._is_heap_satisfied(node.left)
        y_right = Heap._is_heap_satisfied(node.right)

        if node.left:
            left = node.value <= node.left.value and x_left
        if node.right:
            right = node.value <= node.right.value and y_right

        return left and right

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendants = 1
        else:
            self.root = Heap._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        if node is None:
            return
        if node.left and node.right:
            node.left = Heap._insert(node.left, value)
            if node.value > node.left.value:
                return Heap._upHeapBubble(node, value)
        if node.left is None:
            node.left = Node(value)
            if node.value > node.left.value:
                return Heap._upHeapBubble(node, value)
        elif node.right is None:
            node.right = Node(value)
            if node.value > node.right.value:
                return Heap._upHeapBubble(node, value)
        return node

    @staticmethod
    def _upheapBubble(node, value):
        if Heap._is_heap_satisfied(node) is True:
            return node

        if node.left and node.left.value > node.value:
            node.left = Heap._upHeapBubble(node.left, value)
        if node.right and node.right.value > node.value:
            node.right = Heap._upHeapBubble(node.right, value)

        if node.left:
            if node.left.value == value:
                x1 = node.value
                x2 = node.left.value
                node.value = x2
                node.left.value = x1
        if node.right:
            if node.right.value == value:
                x1 = node.value
                x2 = node.right.value
                node.value = x2
                node.right.value = x1

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        '''
        if Heap.is_heap_satisfied(self):
            return self.root.value

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.
        '''
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            self.root = None
        else:
            rightest = Heap._findRight(self.root)
            self.root = Heap._remove(self.root)
            if rightest == self.root.value:
                return
            else:
                self.root.value = rightest

            if Heap._is_heap_satisfied(self.root) is False:
                return Heap._downHeapBubble(self.root)

    @staticmethod
    def _findRight(node):
        if node.left is None and node.right is None:
            return node.value
        elif node.right:
            return Heap._findRight(node.right)
        elif node.left:
            return Heap._findRight(node.left)

    @staticmethod
    def _remove(node):
        if node is None:
            return
        elif node.right:
            node.right = Heap._remove(node.right)
        elif node.left:
            node.left = Heap._remove(node.left)
        else:
            if node.right is None and node.left is None:
                return None
        return node

    @staticmethod
    def _downHeapBubble(node):
        condition1 = (node.left.value <= node.right.value)
        condition2 = (node.right.value <= node.left.value)

        if node.left is None and node.right is None:
            return node
        if node.left and (node.right is None or condition1):
            if node.left.value < node.value:
                x1 = node.value
                x2 = node.left.value
                node.value = x2
                node.left.value = x1
            node.left = Heap._downHeapBubble(node.left)
        elif node.right and (node.left is None or condition2):
            if node.right.value < node.value:
                x1 = node.value
                x2 = node.right.value
                node.value = x2
                node.right.value = x1
            node.right = Heap._downHeapBubble(node.right)

        return node
