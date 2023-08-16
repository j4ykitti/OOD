class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def append_node(head, val):
    new_node = ListNode(val)
    if not head:
        head = new_node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
    return head

def set_next_node(head, index, next_index):
    current = head
    i = 0
    while i < index and current:
        current = current.next
        i += 1

    if not current:
        print(f"Error! {index} not in length")
        return head

    next_node = head
    i = 0
    while i < next_index and next_node:
        next_node = next_node.next
        i += 1

    if not next_node:
        print(f"Error! {next_index} not in length")
        return head

    current.next = next_node
    print(f"Set node.next complete!, index:value = {index}:{current.val} -> {next_index}:{next_node.val}")
    return head

def find_loop(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow

    return None

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print("None")

def find_and_detect_loop(nodes):
    head = None

    for node in nodes:
        operation, *args = node.split()
        if operation == 'A':
            val = int(args[0])
            head = append_node(head, val)
        elif operation == 'S':
            index, next_index = map(int, args[0].split(':'))
            head = set_next_node(head, index, next_index)

    print_linked_list(head)

    loop_node = find_loop(head)

    if loop_node:
        print("Found Loop")
        loop_start = head
        while loop_start != loop_node:
            loop_start = loop_start.next
            loop_node = loop_node.next
        print("Loop starts at:", loop_start.val)
    else:
        print("No Loop")

# Testcases
testcase1 = ['A 0', 'A 1', 'S 2:0']
testcase2 = ['A 0', 'A 1', 'S 0:2']
testcase3 = ['A 0', 'A 1', 'S 1:0']

print("Testcase #1")
find_and_detect_loop(testcase1)

print("\nTestcase #2")
find_and_detect_loop(testcase2)

print("\nTestcase #3")
find_and_detect_loop(testcase3)
