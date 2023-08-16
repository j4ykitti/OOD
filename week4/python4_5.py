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

str = input("Enter width, height, and room: ").split()
width = int(str[0])
height = int(str[1])
room = str[2].split(",")
k= 0
f = 0
x = 0
y = 0
wwe = 0
for i in room:
    for j in i:
        if j == 'F':
            f = 1
            print(f"({x},{y})")
            wwe = 1
        if wwe == 1 :
            if j == '_' :
                if room[x][y-1] == 
            if j == 'O':
                print("Found the exit portal.")
                break
        x += 1
    y += 1
    x = 0




for i in room:
    if len(i) != width or len(room) != height:
        k = 1
if k ==1 or f == 0: print(f"Invalid map input.{x},{y}")

    