#Using collections library to create a stack

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':

    myStack = Stack()

    myStack.push(5)
    myStack.push(4)
    myStack.push(3)
    print("Size: "+str(myStack.size()))
    print("Popped element: "+str(myStack.pop()))
    print("Top of stack: "+str(myStack.peek()))