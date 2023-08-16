def is_balanced(parentheses):
    stack = []
    open_parentheses = ["(", "[", "{"]
    close_parentheses = [")", "]", "}"]
    matches = {"(": ")", "[": "]", "{": "}"}

    for paren in parentheses:
        if paren in open_parentheses:
            stack.append(paren)
        elif paren in close_parentheses:
            if not stack:
                return f"{parentheses} close paren excess"
            top = stack.pop()
            if matches[top] != paren:
                return f"{parentheses} Unmatch open-close"
    
    if stack:
        return f"{parentheses} open paren excess   {len(stack)} : {''.join(stack)}"
    
    return f"{parentheses} MATCH"


test = str(input("test"))
result = is_balanced(test)
print(f"Input: {test}")
print(f"Output: {result}")
print()
