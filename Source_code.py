"""Student Id = 20CE063
    Student name = Preet Padariya"""

# Write a python program to implement a Stack Data structure using the concept of class and object...
# with push, pop and traversal method...

class Stack:
    Data = []
    def push(self, data):
        self.Data.append(data)
    def pop(self):
        if len(self.Data) > 0: 
            return self.Data.pop() 
        else:
            return "stack is empty." 
    def get_stackSize(self):
        return len(self.Data)
    def printStack(self):
        print(self.Data)
        def has_next(self):
            return bool(len(self.Data))
    def next(self):
        return self.pop()
    def peek(self):
        if len(self.Data) > 0: 
            return self.Data[-1] 
        else:
            return "stack is empty." 
    def printPeek(self):
            print(self.peek())
    def printPop(self):
        print(self.pop())

if __name__ == "__main__":
    stack = Stack() 
    stack.printStack()
    stack.push(20)
    stack.printStack()
    stack.push("Preet")
    stack.push("@#$")
    stack.push("21")
    stack.printStack()
    print("pop")
    stack.pop()
    print("peek")
    print(stack.peek())
    stack.printStack()
    print("pop")
    stack.pop()
    print("pop")
    stack.pop()
    print("pop")
    stack.pop()
    stack.printStack()
    print("peek")
    print(stack.peek())
