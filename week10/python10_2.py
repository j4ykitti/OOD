intp = input("Enter Input : ").split("/")
left = [int(i) for i in intp[0].split()]
right = [int(i) for i in intp[1].split()]

for point in right:
    FSV = max(left) + 1
    for ele_val in left:
        if ele_val > point and ele_val < FSV:
            FSV = ele_val
    if FSV > max(left):
        print("No First Greater Value")
    else:
        print(FSV)

