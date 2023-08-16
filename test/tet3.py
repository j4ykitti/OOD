def check_balanced_parentheses(input_string):
    stack = []
    open_parentheses = ["(", "[", "{"]
    close_parentheses = [")", "]", "}"]
    error_message = ""

    for char in input_string:
        if char in open_parentheses:
            stack.append(char)
        elif char in close_parentheses:
            if len(stack) == 0:
                error_message = f"{char} close paren excess"
                break
            else:
                top = stack.pop()
                if open_parentheses.index(top) != close_parentheses.index(char):
                    error_message = f"{top}{char} Unmatch open-close"
                    break

    if len(stack) == 0 and error_message == "":
        return "MATCH"
    elif len(stack) > 0 and error_message == "":
        return f"{input_string} open paren excess\t{len(stack)} : {''.join(stack)}"
    else:
        return error_message


# Test the function with example inputs
test = input()
result = check_balanced_parentheses(test)
print(f"Input: {test}\nOutput: {result}\n")
