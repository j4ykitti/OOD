test = []
# BMI < 18.50 แสดงผล Less Weight

# 18.50 <= BMI  < 23 แสดงผล Normal Weight

# 23 <= BMI  < 25 แสดงผล Morethan Normal Weight

# 25 <= BMI  < 30 แสดงผล Getting Fat

# BMI  >= 30 แสดงผล Fat

test = input("Enter your High and Weight : ")
test1 = test.split()
print(test1)
hh = float(test1[0])
mm = float(test1[1])
res = mm/(hh**2)
if res < 18.5:
    print("Less Weight")
elif res < 23:
    print("Normal Weight")
elif res < 25:
    print("Morethan Normal Weight")
elif res < 30:
    print("Getting Fat")
else:
    print("Fat")