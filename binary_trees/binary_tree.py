class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Public method to insert a value into the tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, current_node):
        """Helper method to find the correct position for the new node."""
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)

    # --- Traversal Methods ---

    def inorder_traversal(self, node):
        """Left -> Root -> Right (Returns sorted values)"""
        if node:
            self.inorder_traversal(node.left)
            print(f"{node.value} ", end="")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        """Root -> Left -> Right"""
        if node:
            print(f"{node.value} ", end="")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        """Left -> Right -> Root"""
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(f"{node.value} ", end="")

# --- Example Usage ---
if __name__ == "__main__":
    bst = BinaryTree()
    data = [50, 30, 70, 20, 40, 60, 80]
    
    for item in data:
        bst.insert(item)

    print("--- Tree Traversals ---")
    print("\nIn-order (Sorted):")
    bst.inorder_traversal(bst.root)
    
    print("\n\nPre-order:")
    bst.preorder_traversal(bst.root)
    
    print("\n\nPost-order:")
    bst.postorder_traversal(bst.root)
