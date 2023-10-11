class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.data)
    
class Linkedlist():
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        result = ''
        cur = self.head
        while cur:
            if cur.next == None:
                result += str(cur.data)
                break
            else : 
                result += str(cur.data) + "->"
                cur = cur.next
        return result
    def str_reverse(self):
        result = ""
        cur = self.tail
        while cur:
            if cur.prev == None:
                result += str(cur.data)
                break
            else :
                result += str(cur.data) + "->"
                cur = cur.prev
        return result
    def isEmpty(self):
        return self.head == None
    
    def append(self, data):
        newnode = Node(data)
        self._size += 1
        if self.isEmpty():
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def add_before(self, item):
        newnode = Node(item)
        self._size += 1
        if self.isEmpty():
            self.head = self.tail = newnode
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head =newnode
    
    def insert(self,pos,item):
        if pos > self.size() or pos <0:
            return print("Data cannot be add")
        if self.isEmpty():
            self.head = self.tail =Node(item)
            self._size+=1
        node = Node(item)
        #push front
        if pos == 0:
            self._size+=1
            node.next = self.head
            self.head.prev = node
            self.head = node
            

        #push back
        if pos == self.size():
            self._size+=1
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        #push at index
        cur = self.head
        index = 0
        while index != pos-1:
            index +=1
            cur = cur.next
        cur.next.prev = node
        node.next = cur.next
        node.prev = cur
        cur.next = node
        self._size += 1


    def size(self):
        return self._size
    
    def remove(self,item):
        if self.isEmpty():
            return print("Not Found!")

        cur = self.head
        if self.size() == 1 and cur.data == item:
            self.head = self.tail = None
            self._size -= 1
            return print(f'removed : {item} from index : 0')
        
        #pop front
        self._size -=1
        if self.head.data == item:
            self.head = self.head.next
            self.head.prev = None
            return print(f'removed : {item} from index : 0')
        
        #pop at index
        index = 0
        while cur.next != None:
            if cur.data == item:
                cur.prev.next,cur.next.prev = cur.next,cur.prev
                return print(f'removed : {item} from index : {index}')
            index += 1
            cur = cur.next

        #pop back
        if cur.data == item:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size += 1
        return print("Not Found!")
    def add(self,value):
        #เพิ่มเข้าลิสเรียงมากไปน้อย
        if self.isEmpty():
            self.head = self.tail = Node(value)
        else: 
            count = 0
            buffer = self.head
            while buffer is not None:
                if buffer.data <= value:
                    self.insert(count,value)
                    return
                count +=1
                buffer = buffer.next
            self.remove(value)
    
        