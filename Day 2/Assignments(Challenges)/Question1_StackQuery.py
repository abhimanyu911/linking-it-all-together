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

    def max(self):
        return max(self.stack)

if __name__ == '__main__':
    print("Enter input in specified format:")
    n = (int)(input())
    ops = []
    for i in range(n):
        ops.append(input())
    
    
    def getMax(operations = None):

        myStack = Stack()
        ele = []

        for op in operations:
            op_arr = list(map(int,op.split()))
            if len(op_arr)==2:
                myStack.push(op_arr[1])
            elif op_arr[0] == 2:
                c= myStack.pop()
            else:
                ele.append(myStack.max())
        
        return ele

    ele = getMax(operations = ops)
    for el in ele:
        print(el)


