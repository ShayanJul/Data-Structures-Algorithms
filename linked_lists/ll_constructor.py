"""linked lists constructor
    """


class Node:
    """this class creates nodes for linked list class
    Node is going to containt a value and next
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """this class creates a linked list
    """

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """this print linked list values
        """
        temp = self.head
        if temp is None:
            print(None)
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """this appends a node to the end of a linked list
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """this pops the last node is a linked list
        """
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """this prepend a value to a linked list
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """this pops the first item of a linked list
        """
        if self.length <= 1:
            return None
        else:
            self.head = self.head.next


my_linked_list = LinkedList(5)
print('Original ll is:')
my_linked_list.print_list()

my_linked_list.append(3)
my_linked_list.append(7)
my_linked_list.append(8)
print('New ll after appending three nodes is:')
my_linked_list.print_list()

my_linked_list.pop()
print('New ll after pop is:')
my_linked_list.print_list()

my_linked_list.prepend(-2)
print('New ll after prepend an item is:')
my_linked_list.print_list()

my_linked_list.pop_first()
print('New ll after popping the first item is:')
my_linked_list.print_list()
