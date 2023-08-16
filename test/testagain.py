class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def createList(l=[]):
    if not l:
        return None

    head = node(l[0])
    cur = head
    for data in l[1:]:
        cur.next = node(data)
        cur = cur.next
    return head

def printList(H):
    cur = H
    while cur:
        print(cur,end = ' ')
        cur = cur.next

def mergeOrderedLists(p, q):
    if p.data < q.data:
        head = node(p.data)
        p = p.next
    else:
        head = node(q.data)
        q = q.next
    cur = head
    while p and q:
        if p.data < q.data:
            cur.next = node(p.data)
            p = p.next
        else:
            cur.next = node(q.data)
            q = q.next
        cur = cur.next
    if p:
        cur.next = p
    elif q:
        cur.next = q

    return head



L1, L2 = input("Enter 2 Lists : ").split()
L1, L2 = list(map(int, L1.split(','))), list(map(int, L2.split(',')))
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('\nLL2 : ',end='')
printList(LL2)
m = mergeOrderedLists(LL1,LL2)
print('\nMerge Result : ',end='')
printList(m)