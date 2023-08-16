print(" *** String count ***")
mes = str(input("Enter message : "))
upper = []
lower = []
for x in range(len(mes)):
    if mes[x].isupper():
        upper.append(mes[x])
    elif mes[x].islower():
        lower.append(mes[x])
Uupper = list(dict.fromkeys(upper))
Ulower = list(dict.fromkeys(lower))
print("No. of Upper case characters :",len(upper))
print("Unique Upper case characters :",*Uupper)
print("No. of Lower case Characters :",len(lower))
print("Unique Lower case characters :",*Ulower)

#  *** String count ***
# Enter message : I Love KMITL.
# No. of Upper case characters : 7
# Unique Upper case characters : I  K  L  M  T  
# No. of Lower case Characters : 3
# Unique Lower case characters : e  o  v  