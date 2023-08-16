print(" *** Wind classification ***")
x = float(input("Enter wind speed (km/h) : "))

	    # Speed (km/h)		ระดับพายุ
		# 	0-51.99			Breeze
		# 	52.00-55.99		Depression
		# 	56.00-101.99	        Tropical Storm
		# 	102.00-208.99	        Typhoon
		# 	>= 209			Super Typhoon
if x < 0:
    print("!!!Wrong value can't classify.")
elif x <= 51.99:
    print("Breeze")
elif x <= 55.99:
    print("Depression")
elif x <= 101.99:
    print("Tropical Storm")
elif x <= 208.99:
    print("Typhoon")
else: print("Super Typhoon")