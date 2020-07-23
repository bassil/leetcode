"""Iterative preorder traversal of binary search tree,
inspired by solution @ https://www.geeksforgeeks.org/iterative-preorder-traversal/"""

from TreeNode import TreeNode

def preorderTraversal(root: TreeNode) -> list:
	"""Iteratively traverse a bst in preorder

	Params
		root - TreeNode

	Output
		preorder - list[int] 
	"""
	if root != None:
		# if root has no children:
		if root.left == None and root.right == None:
			return [root.val]
	else:
		return
		
	preorder = []
	node_stack = []

	# append the root to the stack:
	node_stack.append(root)

	# iterate over node stack until node stack is empty:
	while len(node_stack) > 0:
		current_node = node_stack.pop()

		# add the current node to the preorder
		preorder.append(current_node.val)
		
		# push right child if it exists:
		if current_node.right != None:
			node_stack.append(current_node.right)
			
		# push left child if it exists:
		if current_node.left != None:
			node_stack.append(current_node.left)

	return preorder

# test_1 = TreeNode(1, right=TreeNode(2, TreeNode(3)))

# print(preorderTraversal(root=test_1))