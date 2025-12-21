class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, data):
        self.root = Node(data)

    # -------------------------------------
    # INSERTION
    # -------------------------------------
    def add_node(self, data):
        self.insert(self.root, data)

    def insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(node.left, data)

        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert(node.right, data)

        else:
            print(f"{data} already exists!")

    # -------------------------------------
    # DFS PREORDER (Root, Left, Right)
    # -------------------------------------
    def dfs(self, node=None):
        if node is None:
            node = self.root
        print(node.data)

        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)

    # -------------------------------------
    # INORDER (Left, Root, Right)
    # Sorted output
    # -------------------------------------
    def inorder(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.inorder(node.left)
        print(node.data)
        if node.right:
            self.inorder(node.right)

    # -------------------------------------
    # POSTORDER (Left, Right, Root)
    # -------------------------------------
    def postorder(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.data)

    # -------------------------------------
    # SEARCH
    # -------------------------------------
    def search(self, node, target):
        if node is None:
            return False

        if target == node.data:
            return True
        elif target < node.data:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)

    # -------------------------------------
    # FIND MIN VALUE (Helper for delete)
    # -------------------------------------
    def find_min(self, node):
        while node.left:
            node = node.left
        return node.data

    # -------------------------------------
    # DELETE NODE
    # -------------------------------------
    def delete(self, node, key):
        if node is None:
            return node

        # 1. Search for node
        if key < node.data:
            node.left = self.delete(node.left, key)

        elif key > node.data:
            node.right = self.delete(node.right, key)

        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: Two children
            temp = self.find_min(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)

        return node

    # -------------------------------------
    # VALIDATE BST
    # -------------------------------------
    def is_valid_bst(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True

        if not (min_val < node.data < max_val):
            return False

        return (self.is_valid_bst(node.left, min_val, node.data) and
                self.is_valid_bst(node.right, node.data, max_val))

    # -------------------------------------
    # FIND CLOSEST VALUE
    # -------------------------------------
    def closest_value(self, node, target, closest=None):
        if node is None:
            return closest

        if closest is None or abs(node.data - target) < abs(closest - target):
            closest = node.data

        if target < node.data:
            return self.closest_value(node.left, target, closest)
        else:
            return self.closest_value(node.right, target, closest)


# -------------------------------------
# TESTING THE BST PROGRAM
# -------------------------------------

tree = BST(50)
tree.add_node(40)
tree.add_node(30)
tree.add_node(35)
tree.add_node(60)
tree.add_node(65)
tree.add_node(59)

print("DFS Preorder:")
tree.dfs()

print("\nInorder (sorted):")
tree.inorder()

print("\nPostorder:")
tree.postorder()

print("\nSearch 35:", tree.search(tree.root, 35))
print("Search 100:", tree.search(tree.root, 100))

print("\nClosest to 58:", tree.closest_value(tree.root, 58))

print("\nValidate BST:", tree.is_valid_bst(tree.root))
print("minimum",tree.find_min(tree.root))
print("\nDeleting 40...")
tree.root = tree.delete(tree.root, 40)

print("\nInorder after delete:")
tree.inorder()

