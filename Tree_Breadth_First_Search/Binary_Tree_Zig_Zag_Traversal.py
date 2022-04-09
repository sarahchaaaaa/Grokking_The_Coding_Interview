# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if level == len(result):
                result.append(deque([]))
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].appendleft(node.val)
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level +1])
                
        return result
                
