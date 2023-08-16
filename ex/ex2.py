print("  *** Divisible number ***")
x = int(input("Enter a positive number : "))
if x <= 0 :
    print("{} 0 is OUT of range !!!".format(x))
else: 
    ls = []
 
    for i in range(1,x+1):
        if x % i == 0:
            ls.append(i)
            
    
    total = len(ls)
    
    print("Output ==>",*ls)
    print("Total ==> {}".format(total))
