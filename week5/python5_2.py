class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        result = ""
        current = self.head
        while current:
            if current.next == None:
                result += str(current.data)
                break
            else:
                result += str(current.data) + "->"
                current = current.next
        return result
    
    def str_reverse(self):
        result = ""
        current = self.tail
        while current:
            if current.prev == None:
                result += str(current.data)
                break
            else:
                result += str(current.data) + '->'
                current = current.prev
        return result

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        new_node = Node(data)
        self._size += 1
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def add_before(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self._size += 1
            return

        node = Node(item)
        if self.size() == 1:
            node.next, self.tail.prev, self.head  = self.tail, node, node
        else:
            node.next, self.head.prev, self.head = self.head, node, node
        self._size += 1
    
    def insert(self, pos, item):
        if pos > self.size() or pos < 0:
            return print('Data cannot be added')

        if self.isEmpty():
            self.head = self.tail = Node(item)
            self._size += 1
            return print(f'index = {pos} and data = {item}')

        node = Node(item)
        if pos == 0: #push front
            self._size += 1
            node.next, self.head.prev, self.head = self.head, node, node
            return print(f'index = {pos} and data = {item}')

        if pos == self.size(): #push back
            self._size += 1
            node.prev, self.tail.next, self.tail = self.tail, node, node
            return print(f'index = {pos} and data = {item}')
        #push at index
        cur, index = self.head, 0 
        while index != pos-1:
            index += 1
            cur = cur.next
        
        cur.next.prev = node
        node.next = cur.next
        node.prev = cur
        cur.next = node
        self._size += 1

        return print(f'index = {pos} and data = {item}')

    def size(self):
        return self._size

    def remove(self, item):
        if self.isEmpty():
            return print("Not Found!")

        cur = self.head
        if self.size() == 1 and cur.data == item:
            self.head = self.tail = None
            self._size -= 1
            return print(f'removed : {item} from index : 0')
        
        #pop front
        self._size -= 1
        if item == self.head.data:
            self.head = self.head.next
            self.head.prev = None
            return print(f'removed : {item} from index : 0')

        #pop at index 
        index = 0
        while cur.next != None:
            if cur.data == item:
                cur.prev.next, cur.next.prev = cur.next, cur.prev
                return print(f'removed : {item} from index : {index}')
            index += 1
            cur = cur.next

        #pop back
        if cur.data == item:
            self.tail = self.tail.prev
            self.tail.next = None
            return print(f'removed : {item} from index : {index}')
        self._size += 1
        return print("Not Found!")

if __name__ == '__main__':
    inp = input('Enter Input : ').split(',')

    L = LinkedList()
    for data in inp:
        data = data.split()
        if data[0] == 'A':
            L.append(data[1])
        elif data[0] == 'Ab':
            L.add_before(data[1])
        elif data[0] == 'I':
            L.insert(int(data[1].split(':')[0]), data[1].split(':')[1])
        else:
            L.remove(data[1])
        print('linked list :', L)
        print('reverse :', L.str_reverse())