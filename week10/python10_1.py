intp = input("Enter Input : ").split("/")

def search(n):
    if n == len(intp[0].split(' ')):
        return print("False")
    if intp[0].split(' ')[n] == intp[1]:
        return print("True")
    else: search(n+1)
search(0)