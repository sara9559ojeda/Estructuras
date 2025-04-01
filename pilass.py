class Stack:
    def __init__(self): #constructor
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self, items):
        self.items.append(items)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def top(self):
        if not self.is_empty():
            return self.items[-1]
    def print_stack(self):
        print(self.items)
stack = Stack() 
def is_balanced(expression):
     
    for char in expression:
        if char == '(':  
            stack.push(char)
        elif char == ')':  
            if stack.is_empty():
                return False  
            stack.pop()  

    return stack.is_empty()  


expresiones = ["((2 + 3) * (5 - 1))", "(2 + 3) * (5 - 1))", "((2 + 3) * (5 - 1)" ]

for expr in expresiones:
    print(f"¿La expresión {expr} está balanceada? {is_balanced(expr)}")


