def group_and_count_characters(input_string, pin):
    if pin > len(input_string):
        return "Pin number out of range"
    elif pin < 1:
        return "Pin number less than 1"
    elif not input_string:
        return "List is empty"
    
    grouped_characters = [input_string[i:i+pin] for i in range(0, len(input_string), pin)]
    character_count = len(grouped_characters)
    
    output = f"Character : {grouped_characters[0][0]}\nCount : {character_count}"
    
    return output

input_string = input("Enter string: ")
pin = int(input("Enter pin: "))
result = group_and_count_characters(input_string, pin)
print(result)
