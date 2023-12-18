from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = TreeNode(value=3)
root.left = TreeNode(value=9)
root.right = TreeNode(value=20)
root.right.left = TreeNode(value=15)
root.right.right = TreeNode(value=7)


def maxDepthBFS(root):
    max_depth = 0
    if root is None:
        return max_depth
    q = deque()
    q.append((root, 1))
    while q:
        cur_node, cur_depth = q.popleft()
        max_depth = max(max_depth, cur_depth)
        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth + 1))


print(maxDepth(root))


def maxDepthDFS(root):
    if root is None:
        return 0
    left_depth = maxDepthDFS(root.left)
    right_depth = maxDepthDFS(root.right)
    return max(left_depth, right_depth) + 1
