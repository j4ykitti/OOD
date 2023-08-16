def infix_to_postfix(expression):
    
    result = []
    
    stack = []

    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    
    for token in expression:
        
        if token.isalnum():
            result.append(token)
        
        elif token == '(':
            stack.append(token)
        
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  
        else:
           
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                result.append(stack.pop())
            stack.append(token)

    
    while stack:
        result.append(stack.pop())

   
    return ''.join(result)
infix = input("Enter Infix : ")
postfix_expression = infix_to_postfix(infix)

print(f"Postfix : {postfix_expression}")

