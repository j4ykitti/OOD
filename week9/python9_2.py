def selection(lst):
    for last in range(len(lst) - 1, 0, -1):
        biggest_i = 0
        for i in range(1, last + 1):
            if lst[i] > lst[biggest_i]:
                biggest_i = i
        if biggest_i != last:
            lst[last], lst[biggest_i] = lst[biggest_i], lst[last]
            print(f'swap {lst[biggest_i]} <-> {lst[last]} : {lst}')

lst = [int(x) for x in input('Enter Input : ').split()]
selection(lst)
print(lst)