import QueueLinkedList as queqe

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild =None
        self.rightChild = None
    
Tree = TreeNode('Drink')
leftchild = TreeNode('Hot')
rightchild = TreeNode('Cool')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
leftchild.leftChild = tea
leftchild.rightChild = coffee
Tree.leftChild = leftchild
Tree.rightChild = rightchild

def PreOrederTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    PreOrederTraversal(rootNode.leftChild)
    PreOrederTraversal(rootNode.rightChild)
# PreOrederTraversal(Tree)

def InOrderTraversal(rootNode):
    if not rootNode:
        return
    InOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    InOrderTraversal(rootNode.rightChild)
# InOrderTraversal(Tree)

def PostOrderTraversal(rootNode):
    if not rootNode:
        return
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
# PostOrderTraversal(Tree)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueqe = queqe.Queue()
        customQueqe.enqueue(rootNode)
        while not (customQueqe.isEmpty()):
            root = customQueqe.dequeue()
            print(root.value.data)
            if(root.value.leftChild is not None):
                customQueqe.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQueqe.enqueue(root.value.rightChild)    
# levelOrderTraversal(Tree)
def searchBT(rootNode , nodeValue):
    if not rootNode:
        return "BT does not exist"
    else:
        customQueqe = queqe.Queue()
        customQueqe.enqueue(rootNode)
        while not (customQueqe.isEmpty()):
            root = customQueqe.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if(root.value.leftChild is not None):
                customQueqe.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQueqe.enqueue(root.value.rightChild)    
        return ("Not Found")
print(searchBT(Tree,'Coffesad'))
