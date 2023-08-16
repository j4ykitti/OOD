def odd_list(al):
    js = []
    i = 0
    for i in range(len(al)):
        if al[i]%2 == 1:
            js.append(al[i])
    return js
        
print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)