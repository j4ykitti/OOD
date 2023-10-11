def nameValue(val):
    res = []
    for ele in val:
        res.extend(ord(num) for num in ele)
    return sum(res), val

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self) -> str:
        return self.val[1] + " (" + str(self.val[0]) + ")"

class AVL_Tree(object):
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        
        if data[0] < root.val[0]:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        balance = self.getBalance(root)
        
        if balance > 1:
            if data[0] < root.left.val[0]:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        if balance < -1:
            if data[0] > root.right.val[0]:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root

    def delete(self, root, data):
        if root is None:
            return root
        
        if data[0] < root.val[0]:
            root.left = self.delete(root.left, data)
        elif data[0] > root.val[0]:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def printTree(self, root, level=0):
        if root is None:
            return
        print("    "*level,end="")
        print(root)
        if root.left or root.right:
            if root.left:
                self.printTree(root.left,level + 1)
            else:
                print("    "*(level + 1),end="")
                print("*")
            if root.right:
                self.printTree(root.right,level + 1)
            else:
                print("    "*(level + 1),end="")
                print("*")
        else:
            return

avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    data = nameValue(data)
    if op == "I":
        root = avl_tree.insert(root, data)
    elif op == "D":
        root = avl_tree.delete(root, data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")