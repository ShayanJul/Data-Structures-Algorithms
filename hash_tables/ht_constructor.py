"""Hash tables data structure
    """


class HashTable:
    """This creates a hash table
    """

    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        """Hash method
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        """Prints a hash table
        """
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        """Sets items to a hash table
        """
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """Gets item in a hash table
        """
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def key(self):
        """Gets all the keys in a hash table and puts them into a list
        """
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


my_hash_table = HashTable()
my_hash_table.print_table()

print('Let\'s add items to the hash table:')
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()

print('Let\'s get value for washers')
print(my_hash_table.get_item('washers'))
print('Let\'s get value for lumber')
print(my_hash_table.get_item('lumber'))
print('Let\'s get value for book')
print(my_hash_table.get_item('book'))

print('Let\'s return all the keys of the hash table')
print(my_hash_table.key())
