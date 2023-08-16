test = []
test = input("Enter All Bid : ")
test1 = test.split()
test2 = [int(x) for x in test1]


if len(test2) <= 1:
    print("not enough bidder")
else:
    test2.sort()
    
    if test2[-1] != test2[-2]:
        print("winner bid is {} need to pay {}".format(test2[-1],test2[-2]))
    else:
        print("error : have more than one highest bid")
