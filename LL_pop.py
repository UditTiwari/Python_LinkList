class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        return True
    
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
            
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    
my_linked_list = LinkedList(1)
# print(my_linked_list.head.value)
my_linked_list.append(2)


#(2) iTEMS - Returns 2 node
print(my_linked_list.pop())

#(1) iTEMS - Returns 1 node
print(my_linked_list.pop())

#(0) iTEMS - Returns None
print(my_linked_list.pop())

