# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_left_height(self, root):
        height = 0

        while root:
            height += 1
            root = root.left

        return height

    def find_right_height(self, root):
        height = 0

        while root:
            height += 1
            root = root.right

        return height

    def solution(self,root):

        if not root:
            return 0

        left=self.find_left_height(root)
        right=self.find_right_height(root)

        if left==right:
            return (2**left)-1

        return 1 + self.solution(root.left)+self.solution(root.right)
        

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root and not root.left and not root.right:
            return 1


        return self.solution(root)
        
        

        