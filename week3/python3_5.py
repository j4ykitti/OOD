class Stack():
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,i):
        return self.items.append(i)
    def pop(self):
        return self.items.pop()          

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)       
print("******** Parking Lot ********")
data = input("Enter max of car,car in soi,operation : ").split()
amount = len(data[1].split(","))
# for i in data:
#     print(i)
lst = ((data[1].split(",")))
if data[1] == "0":
    lst = []
test = 1
king = 2
for i in range(0,len(lst)):
    lst[i] = int(lst[i])
# print(lst)

if int(data[0]) == (amount) and data[2] == "arrive":
    print(f"car {data[3]} cannot arrive : Soi Full")
    print(lst)

elif int(data[0]) > (amount) and data[2] == "arrive":
    for i in range(0,amount-1):
        if lst[i] == int(data[3]):
            print(f"car {data[3]} already in soi")
            print(lst)
            test = 0
    if test != 0 :
         print(f"car {data[3]} arrive! : Add Car {data[3]}")
         lst.append(int(data[3]))
         print(lst)

elif data[1] == "0" and data[2] == "depart":
    print(f"car {data[3]} cannot depart : Soi Empty")
    print(lst)

elif data[2] == "depart":
    for i in range(0,amount-1):
        if lst[i] == int(data[3]):
            print(f"car {data[3]} depart ! : Car {data[3]} was remove")
            lst.remove(int(data[3]))
            print(lst)
            king = 1
    if king != 1:
        print(f"car {data[3]} cannot depart : Dont Have Car {data[3]}")
        print(lst)

