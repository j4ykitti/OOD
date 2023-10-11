def is_alphabet(char):
    return 'a' <= char.lower() <= 'z'

def get_first_string_only(str_input):
    for char in str_input:
        if is_alphabet(char):
            return char
    return None

def insertion_sort(lst):
    lst_copy = lst[:]
    for i in range(1, len(lst)):
        current = lst[i]
        j = i
        while j > 0 and lst[j - 1] > current:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = current
    return lst, lst_copy

def find_string_from_char(char, str_input):
    for i in str_input:
        if get_first_string_only(i) == char:
            return i
    return None

def print_list(lst):
    for i in lst:
        print(i, end=" ")
    print()

n = str(input("Enter Input : "))
n = n.split()
sorted_check_list = []
non_sorted_check_list = []
sorted_list = []

for i in n:
    non_sorted_check_list.append(i)
    first_alpha_char = get_first_string_only(i)
    sorted_check_list.append(first_alpha_char)

new_sorted_list, original_list = insertion_sort(sorted_check_list)
for char in sorted_check_list:
    sorted_list.append(find_string_from_char(char, non_sorted_check_list))

print_list(sorted_list)