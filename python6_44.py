def analyze_string(input_str, pin):
    if not input_str:
        return "List is empty"
    
    if pin <= 0:
        return "Pin number must be greater than 0"
    
    if pin > len(input_str):
        return "Pin number out of range"
    
    char_to_find = input_str[pin - 1]
    before_pin = input_str[:pin-1]
    after_pin = input_str[pin:]
    print(before_pin)
    print(after_pin)
    count = before_pin.count(char_to_find) + after_pin.count(char_to_find)
    
    return f"Character : {char_to_find}\nCount : {count}"

# Test cases
test_cases = [
    ("123456789", 3),
    ("12345", 10),
    ("1111111111111111111111111111111111111", 10),
    ("abccasssdacccsd", 4)
    # ("12345", 10),
    # ("", 1),
    # ("sadas", 1),
    # ("asdssscvcsfdadsa", 4),
    # ("65165211233555551", 13)
]

for input_str, pin in test_cases:
    result = analyze_string(input_str, pin)
    print(f"Input number: {input_str}\nOutput: {result}\n")
