#to check whether the parantheses in an expression are balanced using a stack
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, val):
        self.stack.append(val)

    def isEmpty(self):
        return len(self.stack)==0
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

#driver
if __name__ == '__main__':
    print("Enter expression:")
    exp = input()
    flag = True
    myStack = Stack()
    for char in exp:
        if char in ['[', '(', '{'] :
            myStack.push(char)
        #if closing parantheses are encountered, check if popped element is similar parantheses but of opening type
        elif char==')':
            if myStack.pop()!='(':
                flag = False
                break
        elif char=='}':
            if myStack.pop()!='{':
                flag = False
                break
        elif char==']':
            if myStack.pop()!='[':
                flag = False
                break
    if flag:
        print("Balanced")
    else:
        print("Unbalanced")
