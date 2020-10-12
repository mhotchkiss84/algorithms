# Find the greatest common denominator of two numbers
# using Euclid's algorithm

def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b

    return a
    # pass


print(gcd(20, 8))
print(gcd(60, 96))


# Linked list


# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: insert a new node
        new_node = Node(data)

    def find(self, val):
        # TODO: find the first item with a given value
        item = self.head

        return None

    def delete_at(self, idx):
        # TODO: delete an item at given index
        if idx > self.count - 1:
            return

    def dump_list(self):
        temp_node = self.head
        while temp_node is not None:
            print("Node: ", temp_node.get_data())
            temp_node = temp_node.get_next()


# create a linked list and insert some items
item_list = LinkedList()
item_list.insert(38)
item_list.insert(49)
item_list.insert(13)
item_list.insert(15)
item_list.dump_list()

# exercise the list
print("Item count: ", item_list.get_count())
print("Finding item: ", item_list.find(13))
print("Finding item: ", item_list.find(78))

# delete an item
# item_list.deleteAt(3)
# print("Item count: ", item_list.get_count())
# print("Finding item: ", item_list.find(38))
# item_list.dump_list()
