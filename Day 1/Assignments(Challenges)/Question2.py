
#class representing node of a linked list
class Node:

    def __init__(self, data = None, next =  None):
        self.data = data
        self.next = next

#class to represent singly linked list with head pointer
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    #append or insert at end operation
    def append(self, data):

        #if list is empty, first node is added as head
        if self.head is None:
            self.head = Node(data, None)
            return
        
        #iterator
        itr = self.head

        #looking for last element
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
    
    #traversing the list and printing each data item
    def print(self):

        if self.head is None:
            print("Linked List is empty\n")
            return
        
        itr = self.head

        while itr:
            print(itr.data)
            itr = itr.next

if __name__ == '__main__':

    sll = SinglyLinkedList()
    print("Enter input in specified format:")
    p = int(input())
    #constraint 1
    if not(p>=1 and p<=1000):
        print("No of elements out of bounds; start over")
    else:
        flag = True
        for i in range(p):
            q = int(input())
            #constraint 2
            if not(q>=1 and q<=1000):
                print("List element out of bounds; start over")
                flag = False
                break
            else:
                sll.append(q)
        if flag:
            print("Nodes:")
            sll.print()
    