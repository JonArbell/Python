
class Stack:

    def __init__(self):
        self.top = -1
        self.stacks = []

    def isFull(self):
        return self.top == 4

    def isEmpty(self):
        return self.top == -1

    def push(self,value):
        if not self.isFull():
            self.top+=1
            self.stacks.append(value)
            print(f"Pushed: {self.stacks[self.top]}")
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.isEmpty():
            print(f"Popped: {self.stacks[self.top]}")
            del self.stacks[self.top]
            self.top-=1
        else:
            print("Stack Underflow")

    def peek(self):
        if not self.isEmpty():
            print(f"Peak: {self.stacks[self.top]}" )
        else:
            print("Stack Underflow")

    def display(self):

        if not self.isEmpty():
            for stack in self.stacks:
                print(stack)
        else:
            print("Stack Underflow")

stack = Stack()

stack.push(10)
stack.push(15)
stack.push(20)
stack.push(25)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.push(10)
stack.push(15)
stack.push(20)
stack.push(25)
stack.push(30)
stack.push(35)
stack.display()