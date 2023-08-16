class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        self.previous = None

def createList(l = []):
    head = None
    for val in l:
        new_node = Node(val)
        if head is None:
            head = new_node
        else:
            cur = head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
    return head

def printList(cur):
    while cur is not None:
        print(cur.data, end=' ' if cur.next is not None else '\n')
        cur = cur.next

def mergeList(l1, l2):
    dummy = cur = Node(None)
    
    
    while l1:
        cur.next = l1
        l1 = l1.next
        cur = cur.next

    while l2:
        l2 = l2.next
        cur.next = l2
        cur = cur.next

    return dummy.next

inp1, inp2 = input('Enter 2 Lists : ').split()
L1 = [str(x) for x in inp1.split('->')]
L2 = [str(x) for x in inp2.split('->')]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)