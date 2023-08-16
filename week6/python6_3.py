def binary_string(n, current=0):
    if n < 0:
        return ['Only Positive & Zero Number ! ! !']
    elif n == 0:
        return ['0']
    elif current >= 2 ** n:
        return []
    else:
        cur_string = format(current, '0' + str(n) + 'b')
        remain_string = binary_string(n, current + 1)
        return [cur_string] + remain_string

inp = int(input('Enter Number : '))
result = binary_string(inp)
print('\n'.join(result))