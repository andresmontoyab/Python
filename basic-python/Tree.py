from binarytree import Node
from binarytree import build

root = Node(3)
root.left = Node(5)
root.right = Node(9)

print(root)
print("Printing the tree as a List", list(root))
print("Printing the tree as inorder list ", root.inorder)
print("Printing the tree size", root.size)
print("_____________")
nodes = {1,2,3,4,5,6,7,8,9,10,11}
binary_tree = build(nodes)
print("Binary Tree: ", binary_tree)
print("Binary Tree in order: ", binary_tree.inorder)