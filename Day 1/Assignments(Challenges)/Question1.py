class Array:

    def __init__(self):
        self.q = None
        self.array = []

    def reverseArray(self):

        print("Enter input in specified format:\n")

        #type casting the default string input into int
        self.q = int(input())
        
        #constraint 1
        if self.q >=1 and self.q <= 1000:

            #splitting the space-seperated string about the whitespace, mapping to int and storing in a list
            self.array = list(map(int, input().split()))


            for i in range(self.q):
                
                #constraint 2
                if self.array[self.q-1-i]>=1 and self.array[self.q-1-i]<=10000:

                    print(self.array[self.q-1-i], end=" ")

                else:

                    print("<Out of bounds>", end= " ")
        else:
            print("No of elements out of bounds, start over.")

#execute reverseArray() on running script
if __name__=="__main__":
    obj = Array()
    obj.reverseArray()





