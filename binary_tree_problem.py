class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Write function to add Child data to tree
    def add_child(self, data):
        pass

    # Write function to search the tree for 'val'
    def search(self, val):
        pass

    # Write function to perform in-order traversal
    def inorder_traversal(self):
        pass

    # Write function to find max
    def find_max(self):
        pass

    # Write function to find min
    def find_min(self):
        pass

    # Write function to delete 'val' from tree
    def delete(self, val):
        pass


# Build function that will take 'elements' and build the tree
def build_tree(elements):
    print("Building tree:", elements)

    pass


if __name__=='__main__':
    numbers_tree = build_tree([5, 25, 20, 10, 15, 50, 30])
    # Building tree: [5, 25, 20, 10, 15, 50, 30]
    numbers_tree.delete(50)
    print("After deleting 50: ", numbers_tree.inorder_traversal())
    # After deleting 50:  [5, 10, 15, 20, 25, 30, 50]
