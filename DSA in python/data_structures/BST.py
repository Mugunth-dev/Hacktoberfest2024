class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return TreeNode(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

# Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

# Dynamic input
n = int(input("Enter the number of elements in the tree: "))
root = None
for _ in range(n):
    data = int(input("Enter element: "))
    root = insert(root, data)

print("In-order Traversal:", end=' ')
inorder(root)
print("\nPre-order Traversal:", end=' ')
preorder(root)
print("\nPost-order Traversal:", end=' ')
postorder(root)
