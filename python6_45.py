def analyze_string(input_str, pin):
    if not input_str:
        return "Output : List is empty"
    if  pin > len(input_str):
        return "Output : Pin number out of range"
    if  pin < 1 :
        return "Output : Pin number less than 1"
    char_to_find = input_str[pin - 1]
    
    def countingpos(pin1,value1 = 0):
        
        if pin1 >= len(input_str) or input_str[pin1] != char_to_find:
            return value1
        if input_str[pin1] == char_to_find:
            value1 += 1
        return countingpos(pin1+1,value1)
     
    def countingneg(pin2, value2=0):
        if pin2 < 0 or input_str[pin2] != char_to_find:
            return value2
        if input_str[pin2] == char_to_find:
            value2 += 1
        return countingneg(pin2 - 1, value2)
    
    pos = countingpos(pin-1,0)
    neg = countingneg(pin-2,0)
    print(char_to_find,pos,neg)
inp =  input("input number : ").split(',')
str = inp[0]
pin = int(inp[1])
output = analyze_string(str,pin)

