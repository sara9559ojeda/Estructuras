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


numbers = Stack()

numbers.push(9)
numbers.push(10)
numbers.print_stack()
print("-------------")
print ("TOP: ", numbers.top())

numbers.push(15)
numbers.push(16)
numbers.print_stack()
print("-------------")
print ("TOP: ", numbers.top())

numbers.pop()
numbers.pop()
numbers.pop()
print("d,wemcksmckckjfcc")
numbers.print_stack()