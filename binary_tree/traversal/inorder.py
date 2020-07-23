"""Iterative inorder binary search tree traversal,
inspired by solution @ https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/"""

from TreeNode import TreeNode


def inorderTraversal(root: TreeNode) -> list:
	"""Iteratively traversal a bst inorder 

	Params
		root - TreeNode

	Output
		inorder - list[int] 

	"""

	if root != None:
		# if root has no children:
		if root.left == None and root.right == None:
			return [root.val]
	else:
		return

	inorder = []
	# initialize current node as root and push to stack
	current_node = root

	# instantiate a stack
	node_stack = []

	while True:

		# traverse the left children until left-most child
		if current_node != None:
			node_stack.append(current_node)
			current_node = current_node.left

		# visit node at the top of the stack
		elif node_stack:
			current_node = node_stack.pop()
			inorder.append(current_node.val)

			# traverse the right children
			current_node = current_node.right

		else:
			break
			
	return inorder

test_1 = TreeNode(1, right=TreeNode(2, TreeNode(3)))

# test_2 = TreeNode()

# test_3 = None

print(inorderTraversal(root=test_1))