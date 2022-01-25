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

if __name__ == '__main__':

    print("Enter word:")
    word = input()
    myStack = Stack()
    #PUSH ALL CHARACTERS
    for char in word:
        myStack.push(char)
    word_reverse = ""

    #POPPING ALL CHARACTERS RETURNS THEM IN A REVERSE ORDER
    while not(myStack.isEmpty()):
        word_reverse+=myStack.pop()

    if word == word_reverse:
        print("PALINDROME")
    else:
        print("NOT A PALINDROME")