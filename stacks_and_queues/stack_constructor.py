"""stack
    """


class Node:
    """This class creates nodes for stack
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Stack class
    """

    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        """Prints a stack
        """
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        """This pushes an item into a stack
        """

        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        """This pops an item from the top of a stack
        """
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp


print('Let\'s create a stack.')
my_stack = Stack(5)
print('Stack is:')
my_stack.print_stack()

print('Let\'s add three items into the stack')
my_stack.push(3)
my_stack.push(9)
my_stack.push(2)
my_stack.print_stack()

print('Pop two items from the top')
my_stack.pop()
my_stack.pop()
my_stack.print_stack()
