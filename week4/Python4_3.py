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
    
str = input("Enter code,hint : ").split(",")
lst1 = Queqe()
lst2 = Queqe
secret = ord(str[1]) - ord(str[0][0])
for i in range(0,len(str[0])):
    cd = ord(str[0][i]) + secret
    lst1.enQueqe(chr(cd))
    print(lst1.item)

