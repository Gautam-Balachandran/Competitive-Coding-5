# Time Complexity : O(n)
# Space Complexity : O(n)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        if root is None:
            return []

        q = deque([root])
        result = []

        while q:
            h = len(q)
            maxVal = float('-inf')
            for _ in range(h):
                cur = q.popleft()
                maxVal = max(maxVal, cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            result.append(maxVal)

        return result

# Example 1
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

solution = Solution()
print(solution.largestValues(root))  # Output: [1, 3, 9]

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)

solution = Solution()
print(solution.largestValues(root2))  # Output: [1, 3, 5]

# Example 3
root3 = TreeNode(4)
root3.left = TreeNode(9)
root3.right = TreeNode(2)
root3.left.left = TreeNode(3)
root3.left.left.left = TreeNode(1)
root3.left.left.right = TreeNode(6)
root3.right.right = TreeNode(7)
root3.right.right.left = TreeNode(8)
root3.right.right.right = TreeNode(5)

solution = Solution()
print(solution.largestValues(root3))  # Output: [4, 9, 7, 8]