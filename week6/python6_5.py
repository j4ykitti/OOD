def print_stairs(n):
    if n == 0:
        print("Not Draw!")
        return
    
    def print_recursive_positive(row):
        if row > n:
            return
        spaces = '_' * (n - row)
        hashes = '#' * row
        print(spaces + hashes)
        print_recursive_positive(row + 1)

    def print_recursive_neg(row):
        if n >= row:
            return
        spaces = '_' * (row*(-1))
        hashes = '#' * ((n*(-1))+row)
        print(spaces + hashes)
        print_recursive_neg(row -1)
    if n > 0:
        print_recursive_positive(1)
    elif n < 0:
        print_recursive_neg(0)

input_value = int(input("Enter Input : "))
print_stairs(input_value)