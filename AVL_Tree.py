class Node(object):

    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

class AVL_Tree(object):

    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0

    def height(self):
        if self.root:
            return self.root.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return True

    def _insert(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data > node.data:
                node.right = self._insert(node.right, data)
            else:
                node.left = self._insert(node.left, data)
        return node

    def find(self, data):
        return self._find(self.root, data)

    def _find(self, node, data):
        if node is None or node.data == data:
            return True
        elif data > node.data:
            return self._find(node.right, data)
        else:
            return self._find(node.left, data)

    def delete(self, data):
        self.root, deleted = self._delete(self.root, data)
        return deleted

    def _delete(self, node, data):
        if node is None:
            return node, False

        deleted = False
        if data == node.data:
            deleted = True
            if node.right and node.left:
                parant, child = node, node.right
                while node.left is not None:
                    parant, child = child, child.left
                child.left = node.left
                if parant is not node:
                    parant.node = child.right
                    child.right = node.right
                node = child
            elif node.right or node.left:
                node = node.right or node.left
            else:
                node = None
        elif data > node.data:
            node.right, deleted = self._delete(node.right, data)
        else:
            node.left, deleted = self._delete(node.left, data)
        return node, deleted

    def pre_order(self):
        def _pre_order(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order(root.left)
                _pre_order(root.right)
        _pre_order(self.root)

    def in_order(self):
        def _in_order(root):
            if root is None:
                pass
            else:
                _in_order(root.left)
                print(root.data)
                _in_order(root.right)
        _in_order(self.root)

    def post_order(self):
        def _post_order(root):
            if root is None:
                pass
            else:
                _post_order(root.left)
                _post_order(root.right)
                print(root.data)
        _post_order(self.root)

    def level_order(self):
        def _level_order(root):
            data = [root]
            while data:
                root = data.pop(0)
                if root is not None:
                    print(root.data)
                    if root.left:
                        data.append(root.left)
                    if root.right:
                        data.append(root.right)
        _level_order(self.root)

    def rrotate(self):
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_height(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_height()
                if self.node.right != None:
                    self.node.right.update_height()

            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height = -1

    def update_balance(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balance()
                if self.node.right != None:
                    self.node.right.update_balance()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        self.update_height()
        self.update_balance()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def rebalance(self):
        self.update_height(False)
        self.update_balance(False)
        while self.balance < -1 and self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()
                    self.update_height()
                    self.update_balance()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()
                    self.update_height()
                    self.update_balance()


if __name__ == "__main__":
    a = AVL_Tree()
    print()
    "----- Inserting -------"
    # inlist = [5, 2, 12, -4, 3, 21, 19, 25]
    inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    for i in inlist:
        a.insert(i)

    print()
    "----- Deleting -------"
    # a.delete(3)
    # a.delete(4)
    # a.delete(5)

    print()
    print ("Input            :", inlist)
    # print ("deleting ...       ", 3)
    # print ("deleting ...       ", 4)
    print ("in order...     ", a.level_order())