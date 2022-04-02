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
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        """this gets the item by passing an index
        """
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        """This sets a value to an index
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """This inserts a value at an index
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        """This removes an item from an index
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """This reverse a linked list
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# testing the class
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

print('Now let\'s pop first items one by one')
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())

print('Adding some new items \nMy new linked list is:')
my_linked_list.append(-2)
my_linked_list.append(8)
my_linked_list.append(4)
my_linked_list.append(9)
my_linked_list.append(1)
my_linked_list.print_list()

print('Get an item by it\'s index:')
print(my_linked_list.get(2))

print('Set third item with -10:')
my_linked_list.set_value(2, -10)
print('New list is:')
my_linked_list.print_list()

print('Inserting 12 after 2nd item')
my_linked_list.insert(2, 12)
print('New list is:')
my_linked_list.print_list()

print('Let\'s remove the forth item of list')
my_linked_list.remove(3)
print('New list is:')
my_linked_list.print_list()

print('Now let\'s reverse our list')
my_linked_list.reverse()
print('Now list is:')
my_linked_list.print_list()
