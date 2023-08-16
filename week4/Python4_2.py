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
lst1 = Queqe()
lst2 = Queqe()
lst3 = Queqe()
str = input("Enter people : ")
c1 = -1
c2 = -1
for i in range(0,len(str)):
    lst1.enQueqe(str[i])
for i in range(0,len(str)):
    if len(lst2.item) == 0:
        lst2.enQueqe(str[0])
        lst1.deQueqe()
    elif len(lst2.item) < 5 or c1 ==2 :
        lst2.enQueqe(str[i])
        lst1.deQueqe()

    elif len(lst2.item) >= 5 and len(lst3.item) < 5:
        lst3.enQueqe(str[i])
        lst1.deQueqe()
   
    if len(lst2.item) != 0 :
        c1 += 1
    if len(lst3.item) != 0:
        c2 += 1    
    if c1 == 3:
        lst2.deQueqe()
        c1 = 0
    if c2 == 2:
        lst3.deQueqe()
        c2 = 0 
    print(f"{i+1} {lst1.item} {lst2.item} {lst3.item}")