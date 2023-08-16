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
    
# 0,3/0,7/2,3/7,7/10,5/10,1

print(" ***Cafe***")
str = input("Log : ").split("/")
time = 0
no = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
bar1 = Queqe()
bar2 = Queqe()
x = 0
while x != 1:
    for i in str:
        customer = i.split(",")
        no += 1
        if len(bar1.item) < 2 :
            bar1.enQueqe(int(customer[1]))
            if bar1.item[0] - b1 == 0:
                bar1.deQueqe()
                print(f"Time {time} customer {no} get coffee")
            bar1.enQueqe(int(customer[1]))
            if bar1.item[1] - b2 == 0:
                bar1.deQueqe()
                print(f"Time {time} customer {no} get coffee")
        if len(bar1.item) ==0 and len(bar2.item) == 0:
            x = 1
    b1 += 1
    b2 += 1
    time += 1

    
        
        
    print(customer)
