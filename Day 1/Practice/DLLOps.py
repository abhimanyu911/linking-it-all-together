# a class to represent node of a DLL with next and prev pointers
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

#a class to design a DLL with various operations
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #print the list in forward order
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    #print the list in reverse order(back to front)
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    #method to return the last node
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    #method to get the length of the list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    #insert element at beginning of list
    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    #insert element at the end of the list
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    #insert at a specific index    
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    #deletion at a specific index
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    #append operation
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()