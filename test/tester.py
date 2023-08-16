class Queue:
    def __init__(self):
        self.queue = []

    def push(self,data):
        self.queue.append(data)

    def pop(self):
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True
        
    def __str__(self):
        return "[" + ", ".join(str(i) for i in self.queue) + "]"
    
print(" ***Cafe***")
cafe_queue = input("Log : ").split("/")

customers = [[int(x) for x in i.split(",")] for i in cafe_queue]

for i in range(len(customers)):
    customers[i] = customers[i] + [i + 1]

customers = sorted(customers, key=lambda x: (x[0], x[2]))

# print(customers)

queue = Queue()

for i in customers:
    queue.push(i)

balista1 = []
balista2 = []

customer_wait = 0
longest_wait = 0
timer = 0

# print(queue)

while(not queue.isEmpty()):     
    current = queue.pop()
    if not balista1 :
        coffee = current[1] + current[0]
        balista1.append([coffee,current[2]])
    elif not balista2 :
        coffee = current[1] + current[0]
        balista2.append([coffee,current[2]])
    else:
        if balista1[-1][0] <= balista2[-1][0]:
            start_time = current[0]
            if start_time >= balista1[-1][0]:
                coffee = start_time + current[1]
            else:
                coffee = balista1[-1][0] + current[1]
                wait = balista1[-1][0] - start_time
                if wait > longest_wait:
                    longest_wait = wait
                    customer_wait = current[2]
            balista1.append([coffee,current[2]])
        else:
            start_time = current[0]
            if start_time >= balista2[-1][0]:
                coffee = start_time + current[1]
            else:
                coffee = balista2[-1][0] + current[1]
                wait = balista2[-1][0] - start_time
                if wait > longest_wait:
                    longest_wait = wait
                    customer_wait = current[2]
            balista2.append([coffee,current[2]])
        
# print("B1 : ",end="")
# print(balista1)
# print("B2 : ",end="")
# print(balista2)

ans = balista1 + balista2
ans.sort()

# print(ans)
for i in range(len(ans)):
    print(f"Time {ans[i][0]} customer {ans[i][1]} get coffee")

if longest_wait == 0:
    print("No waiting")
else:
    print(f"The customer who waited the longest is : {customer_wait}")
    if longest_wait > 1 :
        print(f"The customer waited for {longest_wait} minutes")
    else:
        print(f"The customer waited for {longest_wait} minute")
# 1
# 2