"""queue
    """


class Node:
    """This creates node for queue
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """queue constructor
    """

    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        """Prints a queue
        """
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        """This enqueue items into a queue
        """
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        """This dequeue item from a queue
        """
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1
        else:
            self.first = self.first.next
            temp.next = None
            self.length -= 1
            return temp


print('Let\'s create a queue')
my_queue = Queue(7)
print('Queue is:')
my_queue.print_queue()

print('Let\'s add three items into the queue')
my_queue.enqueue(3)
my_queue.enqueue(-2)
my_queue.enqueue(9)
print('Queue is:')
my_queue.print_queue()

print('Let\'s dequeue two items')
my_queue.dequeue()
my_queue.dequeue()
print('Queue is:')
my_queue.print_queue()
