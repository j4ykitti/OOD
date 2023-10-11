class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

def create_binary_tree(values):
    root = None
    for value in values:
        root = insert(root, value)
    return root

# Example usage:
input_values = [5, 4, 3, 2, 1]
root = create_binary_tree(input_values)
print_tree(root)

input_values = [4, 5, 3, 1, 2]
root = create_binary_tree(input_values)
print_tree(root)

input_values = [100, 120, 110, 110, 130, 90, 60, 70, 75, 74, 76]
root = create_binary_tree(input_values)
print_tree(root)
