class Queue:
    def __init__(self, q = None):
        if q == None:
            self.item = []
        else:
            self.item = q
    def enQueue(self, i):
        self.item.append(i)
    def deQueue(self):
        return self.item.pop(0)
    def isEmpty(self):
        return self.item == []
    def size(self):
        return len(self.item)

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root = self._insert(self.root,data)

    def level_order(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        q = Queue()
        q.enQueue(self.root)
        while q.isEmpty() is not True :
            n = q.deQueue()
            if n.left is None:
                n.left = Node(data)
                return
            if n.right is None:
                n.right = Node(data)
                return
            if n.left is not None:
                q.enQueue(n.left)
            if n.right is not None:
                q.enQueue(n.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def max_path(self, root):
        path = []
        self.all_path(self.root, path, 0)

    def all_path(self, root, path, pathlen):
        # global lst
        if root == None:
            return
        if(len(path) > pathlen):
            path[pathlen] = root.data
        else:
            path.append(root.data)
        
        pathlen += 1
        if root.left == None and root.right == None:
            # lst.append(path)
            self.printArray(path, pathlen)
        else:
            self.all_path(root.left, path, pathlen)
            self.all_path(root.right, path, pathlen)

    def printArray(self, ints, len):
        global lst
        path = []
        for i in ints[0 : len]:
            path.append(i)
        lst.append(path)

    # def postOrder(self):
    #     Tree._postOrder(self.root)

    # def _postOrder(root):
    #     if root is not None:
    #         Tree._postOrder(root.left)
    #         Tree._postOrder(root.right)
    #         print(root, end = ' ')

T = Tree()
inp = [int(i) for i in input('Enter tree: ').split()]
lst = []
sum_lst = []
for i in inp:
    root = T.level_order(i)
# T.printTree(T.root)
T.max_path(T.root)
# print(lst)
for i in lst:
    sum_lst.append(sum(i))
# print(sum_lst)
print("Maximum path:",lst[sum_lst.index(max(sum_lst))])
