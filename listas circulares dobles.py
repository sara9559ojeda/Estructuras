class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None
class CircularDoubleLinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.next = self.head
            new_node.prev = last
            self.head.prev = new_node
    def delete(self, data):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        if current.data == data:
            if current.next == self.head:
                self.head = None
            else:
                last = self.head.prev
                self.head = current.next
                self.head.prev = last
                last.next = self.head
            return
        while current.next != self.head:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next
        if current.data == data:
            current.prev.next = self.head
            self.head.prev = current.prev
            return
                
                
    def print_list(self, my_list):
        current = my_list.head
        if current is not None:
            print(current.data)
            current =current.next
        while current != my_list.head:
            print(current.data)
            current = current.next
my_list = CircularDoubleLinkedList()

my_list.insert_at_beginning(1)
my_list.insert_at_end(2)
my_list.insert_at_beginning(3)
my_list.insert_at_end(4)

my_list.print_list(my_list)

my_list.delete(1)

my_list.print_list(my_list)

