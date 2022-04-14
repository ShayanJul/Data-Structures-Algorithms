"""Binary search tree data structure
    Trees are similar to linked lists but they have a left and a right
    """


class Node():
    """This creates a node for tree data structure
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    """This is a tree constructor
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert an item into a bst
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while True:
                if new_node == temp:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    def contains(self, value):
        """If a tree contains a particular value
        """
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BinarySearchTree()
print(my_tree.root)

print('Let\'s add 2, 1, 3 to the tree.')
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print('Does my tree contain 2 ?')
print(my_tree.contains(2))
