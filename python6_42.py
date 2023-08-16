def analyze_string(input_str, pin):
    if not input_str:
        return "Output : List is empty"

    if  pin > len(input_str):
        return "Output : Pin number out of range"
    if  pin < 1 :
        return "Pin number out of rangeei"

    char_to_find = input_str[pin - 1]
    char_count = input_str.count(char_to_find)

    result = f"Character : {char_to_find}\nCount : {char_count}"
    return result

test_cases = input("input number : ").split( ",")
test_cases[1] = int (test_cases[1])

  
output = analyze_string(test_cases[0], test_cases[1])
print(output)   

# for input_str, pin in test_cases:
#     result = analyze_string(input_str, pin)
#     print(f"Input number: {input_str}, Pin: {pin}\nOutput: {result}\n")
