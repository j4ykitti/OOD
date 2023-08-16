print("*** Election ***")
check = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
num = input("Enter a number of voter(s) : ")

vote = input().split(" ")
vote = [int(x) for x in vote]
max = 0
leader = []
for i in range(len(vote)):
    if vote[i] <= 20 and vote[i] >= 1:
         check[vote[i]-1] += 1
for j in check:
     if j > max:
          max = j
for k in range(0,19):
     if max == check[k]:
          leader.append(k + 1)
if max > 0:
     print(' '.join(str(x) for x in leader))
else:
     print("*** No Candidate Wins ***")