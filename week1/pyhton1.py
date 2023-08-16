test = []
print("Enter hh mm ss :")
test = input("")
test1 = test.split()
print(test1)
hh = int(test1[0])
mm = int(test1[1])
ss = int(test1[2])
result = hh*3600 + mm*60 + ss
print(f"{hh:02d}:{mm:02d}:{ss:02d} = {result:,} seconds")