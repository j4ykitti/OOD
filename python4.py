class Queqe:
    def __init__(self, list = None):
        if list == None:
            self.item = []
        else: 
            self.item = list
    def enQueqe(self,i):
        self.item.append(i)
    
    def deQueqe(self):
        return self.item.pop(0)
    
    def isEmpty(self):
        return self.item == []
    
    def size(self):
        return len(self.item)


q = Queqe(['a','b','c'])
print(q.item)
q.enQueqe('d')
print(q.item)
q.deQueqe()
print(q.item)
print(q.size)