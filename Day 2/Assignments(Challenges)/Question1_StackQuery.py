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

#driver code
if __name__ == '__main__':
    flag_typ = True
    flag_ele =  True
    print("Enter input in specified format:")
    n = (int)(input())

    #constraint 1
    if n>=1 and n<=10**5:
        ops = []
        for i in range(n):
            temp = input()
            ops.append(temp)
            temp_arr = list(map(int,temp.split()))
            #constraint 2
            if not(temp_arr[0]>=1 and temp_arr[0]<=3):
                flag_type = False
                print("Invalid type entered, start over")
                break
            #constraint 3
            if not(temp_arr[1]>=1 and temp_arr[1]<=10**9):
                flag_ele = False
                print("Invalid element, start over")
                break
    
    
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

        if flag_typ and flag_ele:
            ele = getMax(operations = ops)
            for el in ele:
                print(el)
    else:
        print("Invalid no of queries, start over")


