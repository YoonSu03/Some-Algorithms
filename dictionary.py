def make_askii(word):
    res = ''
    for l in word:
        res += str(ord(l))
    return int(res)

class Node(object):

    def __init__(self, data, mean):
        self.word = data
        self.left = self.right = None
        self.data = make_askii(data)
        self.mean = mean

class BinarySearchTree(object):

    def __init__(self):

        self.root = None

    def insert(self, data, mean):
        self.root = self._insert_value(self.root, data, mean)
        return self.root is not None

    def _insert_value(self, node, data, mean):
        if node is None:
            node = Node(data, mean)
        else:
            if make_askii(data) <= node.data:
                node.left = self._insert_value(node.left, data, mean)
            else:
                node.right = self._insert_value(node.right, data, mean)
        return node

    def find(self, key):
        return self._find_value(self.root, make_askii(key))

    def _find_value(self, root, key):
        if root is None or root.data == key:
            try:
                return root.mean
            except:
                return ('word is not in dictionary.')
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, make_askii(key))
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.word + ':', root.mean)

                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)

    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.word + ':', root.mean)

                _in_order_traversal(root.right)

        _in_order_traversal(self.root)

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.word + ':', root.mean)

        _post_order_traversal(self.root)

    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.word+':', root.mean)
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)

# f = open("words.txt", 'r')
# words = []
# while True:
#     line = f.readline()
#     if not line: break
#     line = line.split()
#     words.append((line[0], ' '.join(line[1:])))
# f.close()
#
# import random
# random.shuffle(words)
#
# Dictionary = BinarySearchTree()
# for word, mean in words:
#     Dictionary.insert(word, mean)
#
# import pickle
#
# with open('data.pickle', 'wb') as f:
#     pickle.dump(Dictionary, f, pickle.HIGHEST_PROTOCOL)

import pickle

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

data.level_order_traversal()
print(data.find('fo'))