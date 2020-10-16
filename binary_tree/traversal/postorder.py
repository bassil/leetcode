"""Traversal of a binary search tree in postorder,
inspired by solution @ https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/"""

from TreeNode import TreeNode

def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def postorderTraversal(root:TreeNode) -> list:
    """Iteratively traverse a bst in postorder 

    Params
        root - TreeNode

    Output
        postorder - list[int] 

    """

    if root != None:
        # if root has no children:
        if root.left == None and root.right == None:
            return [root.val]
    else:
        return

    postorder = []

    # initialize current node as root and push to stack
    current_node = root

    # instantiate a stack
    node_stack = []

    while True:
        while current_node:
            if current_node.right != None:
                node_stack.append(current_node.right)

            node_stack.append(current_node)

            current_node = current_node.left

        current_node = node_stack.pop()

        if current_node.right != None and peek(node_stack) == current_node.right:
            node_stack.pop()
            node_stack.append(current_node)
            current_node = current_node.right

        else:
            postorder.append(current_node.val)
            current_node = None

        if len(node_stack) <= 0:
            break

    return postorder

test_1 = TreeNode(1, right=TreeNode(2, TreeNode(3)))

# test_2 = TreeNode()

# test_3 = None

print(postorderTraversal(root=test_1))