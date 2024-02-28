
import random
from recorrer import inorder_traversal
from tree_node import TreeNode


def create_tree_binary_search(lista: list) -> TreeNode:

    if not lista:
        return None
    
    random.shuffle(lista)
    
    root = TreeNode(lista[0])
    for i in range(1, len(lista)):
        root = insert_into_binary_tree(root, lista[i])
    
    return root

def insert_into_binary_tree(root: TreeNode, item: int) -> TreeNode:
    if root is None:
        return TreeNode(item)

    if item < root.val:
        root.left = insert_into_binary_tree(root.left, item)
    elif item >= root.val:
        root.right = insert_into_binary_tree(root.right, item)

    return root

a = [5, 2, 8, 1, 9, 7, 3, 4, 10, 6 ]
print(inorder_traversal(create_tree_binary_search(a)))

