class Node:

    def __init__(self, my_key): # Constructor for the Node.
        self.key = my_key       # Set the key to my_key
        self.left = None        # Set left child to None
        self.right = None       # Set right child to None

    def insert(self, key_to_insert):

        if (key_to_insert == self.key):
            return

        if (key_to_insert < self.key):
            if (self.left == None):
                self.left = Node(key_to_insert)
            else:
                self.left.insert(key_to_insert)
            return

        if (key_to_insert > self.key):
            if (self.right == None):
                self.right = Node(key_to_insert)
            else:
                self.right.insert(key_to_insert)
            return


    def inorder_traversal(self, ret_list):

        if (self.left != None):
            self.left.inorder_traversal(ret_list)

        ret_list.append(self.key)

        if (self.right != None):
            self.right.inorder_traversal(ret_list)


    def get_depth(self):

        if (self.left == None and self.right == None):
            return 1

        if (self.left != None and self.right == None):
            return 1 + self.left.get_depth()

        if (self.left == None and self.right != None):
            return 1 + self.right.get_depth()

        if (self.left != None and self.right != None):
            return 1 + max(self.left.get_depth(), self.right.get_depth())

    def key_exists(self, key_to_find):

        nodes = []
        self.inorder_traversal(nodes)

        for i in nodes:
            if (i == key_to_find):
                return True
        return False

if __name__ == '__main__':
    tree = Node(7)
    for x in range(20):
        tree.insert(x)

    nodes = list()
    tree.inorder_traversal(nodes)
    print("Nodes: ", nodes)
    print("Depth: ", tree.get_depth())
