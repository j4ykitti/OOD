class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self, lst=[]):
        
        self.head = None
        self.tail = None
        self.size = 0
        if lst != []:
            for num in lst:
                self.append(Node(num))
      
    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
        
        return node

    def prepend(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1
        return node

    def __deleteOne(self):
        temp = self.head
        self.head = None 
        self.tail = None
        self.size -= 1
        return temp
    
    def pop(self):
        if self.head == None:
            return None 
        if self.head == self.tail:
            return self.__deleteOne()
        last = self.tail 
        self.tail = self.tail.prev
        self.tail.next = None
        last.prev = None
        self.size -= 1
        return last
    
    def popLeft(self):
        if self.head == None:
            return None
        if self.head == self.tail:
            return self.__deleteOne()
        left = self.head
        self.head = self.head.next
        self.head.prev = None
        left.next = None
        self.size -= 1
        return left
    
    def moveToHeadRev(self, ll2):
        while ll2.head:
            self.prepend(ll2.popLeft())
            
    def moveToHead(self, ll2):
        while ll2.tail:
            self.prepend(ll2.pop())
    
    def isEmpty(self):
        return self.head == None
    
    def out(self):
        res = ""
        cur = self.head 
        while cur != None:
            res += str(cur.val) + " -> "
            cur = cur.next
        return res[:-4]
    
    def printBackward(self):
        res = ""
        cur = self.tail
        while cur != None:
            res += str(cur.val) + " "
            cur = cur.prev
        return res
    
    def __str__(self):
        res = ""
        cur = self.head 
        while cur != None:
            res += str(cur.val) + " "
            cur = cur.next
        return res
    
    def __len__(self):
        return self.size
    
def countDigit(num):
    num = abs(num)
    i=0
    while num > 0:
        num = num//10
        i+=1
    return i

def getMaxDigit(nums):
    max = 0
    for num in nums:
        digits = countDigit(num)
        if digits > max:
            max = digits
    return max

def getNumAt(digit, num):
    num = abs(num)
    i=0
    res = -1
    while i<digit:
        res = num%10
        num = num//10
        i+=1
    return res
    
def radixSort(nums):
    max_digit = getMaxDigit(nums)
    length = len(nums)
    check = 0
    ll = LinkedList(nums)
    pos = [LinkedList() for i in range(100)]
    neg = [LinkedList() for i in range(100)]
    before = "Before Radix Sort : " + ll.out()
    
    for digit in range(1, max_digit+2):
        while not ll.isEmpty():
            node = ll.popLeft()
            num = node.val
            index = getNumAt(digit, num)
            if num<0:
                neg[index].append(node)
            else:
                pos[index].append(node)
        if digit == max_digit+1: 
            for i in range(10):
                ll.moveToHeadRev(pos[i])
                ll.moveToHead(neg[i])
            break
        print(f"Round : {digit}")
        for i in range(10):
            print(f"{i} : {neg[i]}{pos[i].printBackward()}")
            ll.moveToHead(neg[i])
            ll.moveToHead(pos[i])
        print("------------------------------------------------------------")
    print(f"{digit-1} Time(s)")
    print(before)
    print(f"After  Radix Sort : {ll.out()}")

inp = input("Enter Input : ").split()
nums = [int(x) for x in inp]
print("------------------------------------------------------------")
radixSort(nums)