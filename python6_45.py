def analyze_string(input_str, pin):
    if not input_str:
        return "Output : List is empty"
    if  pin > len(input_str):
        return "Output : Pin number out of range"
    if  pin < 1 :
        return "Output : Pin number less than 1"
    char_to_find = input_str[pin - 1]
    
    def countingpos(pin1,value1 = 0):
        if value1 == 0:
            x1 = 0
        if input_str[pin1] != char_to_find:
            return x1
        if input_str[pin1] == char_to_find:
            x1 += 1
        countingpos(pin1+1)
    def countingneg(pin2,value2 = 0):
        if value2 == 0:
            value2 = 0
        if input_str[pin2] != char_to_find:
            return value2
        if input_str[pin2] == char_to_find:
            value2 += 2
        countingneg(pin2-1)    
    
    
    print(char_to_find,countingpos(pin-1),countingneg(pin-2))
inp =  input("input number : ").split(',')
str = inp[0]
pin = int(inp[1])
output = analyze_string(str,pin)
print(output)
