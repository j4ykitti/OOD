class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.isBurn = False

    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self._add(self.root, data, None)

    def _add(self, root, data, parent):
        if root is None:
            return Node(data, parent)

        if data < root.data:
            root.left = self._add(root.left, data, root)
        else:
            root.right = self._add(root.right, data, root)

        balance_factor = self.get_balance_factor(root)

        if balance_factor > 1 and data < root.left.data:
            return self.rotate_right(root)
        if balance_factor < -1 and data >= root.right.data:
            return self.rotate_left(root)
        if balance_factor > 1 and data >= root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance_factor < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def rotate_left(self, root):
        temp_node = root.right
        root.right = temp_node.left
        if temp_node.left:
            temp_node.left.parent = root
        temp_node.parent = root.parent
        root.parent = temp_node
        temp_node.left = root
        return temp_node

    def rotate_right(self, root):
        temp_node = root.left
        root.left = temp_node.right
        if temp_node.right:
            temp_node.right.parent = root
        temp_node.parent = root.parent
        root.parent = temp_node
        temp_node.right = root
        return temp_node

    def get_height(self, root):
        if root is None:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        return max(left_height, right_height) + 1

    def get_balance_factor(self, root):
        if root is None:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        return left_height - right_height

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        if node:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node, node.parent)
            self.print_tree(node.left, level + 1)

    def find_data(self, data):
        return self._find_data(self.root, data)

    def _find_data(self, root, data):
        if root is None:
            return None

        if root.data == data:
            return root

        left_result = self._find_data(root.left, data)
        if left_result:
            return left_result

        return self._find_data(root.right, data)

    def burn_tree(self, root):
        queue = [(0, [root])]
        visited = set()

        while queue:
            time, nodes = queue.pop(0)
            print(" ".join(str(node) for node in nodes))

            next_nodes = []
            for node in nodes:
                node.isBurn = True
                visited.add(node)
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in visited:
                        next_nodes.append(neighbor)

            if next_nodes:
                queue.append((time + 1, next_nodes))

data_str, target = input("Enter node and burn node : ").split('/')
datas = list(map(int, data_str.split()))
target = int(target)

avl = AVL()

for data in datas:
    avl.add(data)

node_target = avl.find_data(target)

if node_target is not None:
    avl.burn_tree(node_target)
else:
    print(f"There is no {target} in the tree.")