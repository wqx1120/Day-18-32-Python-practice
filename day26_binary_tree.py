class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def preorder(node):
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

def postorder(node):
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]

print("Preorder:", preorder(root))   # [1, 2, 4, 5, 3]
print("Inorder:", inorder(root))     # [4, 2, 5, 1, 3]
print("Postorder:", postorder(root)) # [4, 5, 2, 3, 1]



#leetcode 104 Maximum Depth of Binary Tree
#DFS
#O(n), visit each node once
#O(h), h is the height of the tree, O(n) in worst case (skewed tree)
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

#BFS
#O(n), visit each node once
#O(n), in the worst case, the last level has n/2 nodes
from collections import deque
def maxDepthBFS(root: TreeNode) -> int:
    if not root:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)


print("DFS Max Depth:", maxDepth(root))
print("BFS Max Depth:", maxDepthBFS(root))