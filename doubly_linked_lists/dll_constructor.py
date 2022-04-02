"""Doubly linked lists constructor
    """


from statistics import median


class Node:
    """This creates a single doubly node
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Doubly linked list constructor
    """

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """This prints a list
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """This appends an item to a doubly linked list
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """This pops the last item of a doubly linked list
        """
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        """This prepend an item to a doubly linked list
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """This pops the first item from a doubly linked list
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
        """This gets an item of a dll by its index
        """
        if index < 0 or index >= self.length:
            return None
        if index <= self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(index):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        """This sets value of an index
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """This insert a value at an specific index
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index - 1)
            after = before.next
            new_node.prev = before
            new_node.next = after
            after.prev = new_node
            before.next = new_node
            self.length += 1
        return True


my_doubly_list = DoublyLinkedList(7)
print('My list is:')
my_doubly_list.print_list()

print('Appending 5, -2, 8, 10, 12 to the list')
my_doubly_list.append(5)
my_doubly_list.append(-2)
my_doubly_list.append(8)
my_doubly_list.append(10)
my_doubly_list.append(12)
print('My list is:')
my_doubly_list.print_list()

print('let\'s pop two items of the list:')
my_doubly_list.pop()
my_doubly_list.pop()
print('My list is:')
my_doubly_list.print_list()
my_doubly_list.pop_first()
print('Let\'s prepend -3, 8 to the list')
my_doubly_list.prepend(-3)
my_doubly_list.prepend(8)
print('My list is:')
my_doubly_list.print_list()

print('Now we pop two first items')
my_doubly_list.pop_first()
my_doubly_list.pop_first()
print('My list is:')
my_doubly_list.print_list()

print('The second item of the list is:')
print(my_doubly_list.get(1))

print('Let\'s change the third item to -5')
my_doubly_list.set_value(2, -5)
print('My list is:')
my_doubly_list.print_list()

print('Insert 12 after second item')
my_doubly_list.insert(2, 12)
print('My list is:')
my_doubly_list.print_list()
