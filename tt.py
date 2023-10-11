lst = [0,1]+[-1]*1000000
def fibo(n):
    if lst[n] != -1:
        return lst[n]
    lst[n] = fibo(n-1) + fibo(n-2)
    if n <= 1:
        return 1
    else: return lst[n-1] + lst[n-2]

print(fibo(6))

