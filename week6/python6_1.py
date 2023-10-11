def fibo(n):  # should use dp to make it faster
    if n == 1 or n == 0:  # base case
        return n
    else:  # recursive case
        return fibo(n-1) + fibo(n-2)  # redundant call (multiple calls to calculated value)


lst = [0, 1]+[-1]*1000000


def dp_fibo(n):
    global lst
    if lst[n] != -1:
        return lst[n]

    lst[n] = dp_fibo(n-1) + dp_fibo(n-2)  # building the list for dp
    if n <= 1:
        return 1
    else:
        return lst[n-1] + lst[n-2]


if __name__ == '__main__':
    
    to_go = 100
    i = int(input("Enter Number : "))
   
    print(f'fibo({i}) = {dp_fibo(i)}')