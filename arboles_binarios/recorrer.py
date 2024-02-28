import queue

from tree_node import TreeNode

def breadth_first_search(root: TreeNode) -> list:
    queue_implemnt = queue.Queue()
    result = []

    queue_implemnt.put(root)

    while not queue_implemnt.empty():
        node = queue_implemnt.get()
        result.append(node.val)
        if node.left:
            queue_implemnt.put(node.left)
        if node.right:
            queue_implemnt.put(node.right)

    return result

def preorder_traversal(root: TreeNode) -> list:
    if root is None:
        return []
    return ( [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right))

def postorder_traversal(root: TreeNode) -> list:
    if root is None:
        return []
    return (postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val])

def inorder_traversal(root: TreeNode) -> list:
    if root is None:
        return []
    return (inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right))



# Construir un árbol binario
#        5
#       /  \
#      2    6
#     / \    \
#    1   4     9
#       / \   / \
#      8   3  0  7

 
'''root = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(9)
root.right.left.left = TreeNode(0)
root.right.left.right = TreeNode(7)'''

root = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.right.right = TreeNode(4)

root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(9)
root.right.right.right = TreeNode(10)

#print(breadth_first_search(root))
#print(preorder_traversal(root))
#print(postorder_traversal(root))
#print(inorder_traversal(root))



