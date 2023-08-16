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
q = Queqe()
count = 0
test = input("Enter Input : ").split(",")
for i in range(0,len(test)):
    exp = test[i].split()
    if exp[0] == 'E':
        q.enQueqe(exp[1])
        print(q.size())
    if exp[0] == 'D':
        if len(q.item) != 0:
         return_value = q.deQueqe()
         print(f"{return_value} 0")
        else: print("-1")
        
if len(q.item) != 0:
    print(*q.item)

else :
    print("Empty")