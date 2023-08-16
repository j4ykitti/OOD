inp=int(input("Enter year : "))
for i in range(2, int(inp/2)+1):
    base = 2*i
    if base+1==inp :
        print(f"saimai is just 21, in base {i}!")
        break
    elif base == inp:
        print(f"saimai is just 20, in base {i}!")