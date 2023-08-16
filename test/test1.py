class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_linked_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    l2 = reverse_linked_list(l2)

    current = l1
    while current.next is not None:
        current = current.next

    current.next = l2

    return l1

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" "if current.next is not None else '\n')
        current = current.next
    


def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    inp1, inp2 = input('Enter Input (L1,L2) : ').split()
    L1 = [str(x) for x in inp1.split('->')]
    L2 = [str(x) for x in inp2.split('->')]
    list1 = create_linked_list(L1)
    list2 = create_linked_list(L2)

    print("L1    : ",end='')
    print_linked_list(list1)
    print("L2    : ",end='')
    print_linked_list(list2)

    merged_list = merge_linked_lists(list1, list2)

    print("Merge : ",end='')
    print_linked_list(merged_list)
