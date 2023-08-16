def infix_to_postfix(expression):
    # ตัวแปรเก็บผลลัพธ์
    result = []
    # Stack สำหรับเก็บตัวดำเนินการ
    stack = []

    # กำหนดความสำคัญของตัวดำเนินการ
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # วนลูปตามสมาการใน expression
    for token in expression:
        # ถ้า token เป็นตัวเลขหรือตัวอักษร
        if token.isalnum():
            result.append(token)
        # ถ้า token เป็นเครื่องหมายเปิดวงเล็บ
        elif token == '(':
            stack.append(token)
        # ถ้า token เป็นเครื่องหมายปิดวงเล็บ
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # นำวงเล็บเปิดออกจาก stack
        else:
            # ถ้า token เป็นตัวดำเนินการ
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                result.append(stack.pop())
            stack.append(token)

    # นำตัวดำเนินการที่เหลืออยู่ใน stack มาต่อท้ายผลลัพธ์
    while stack:
        result.append(stack.pop())

    # รวมผลลัพธ์เป็นสตริงเดียว
    return ''.join(result)

# ตัวอย่างการใช้งาน
test = input()

postfix_expression = infix_to_postfix(test)
print(postfix_expression)
