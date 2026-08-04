# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # def find_height(root):
        #     if not root:
        #         return 0

        #     lf=find_height(root.left)
        #     rt=find_height(root.right)

        #     return max(lf,rt)+1

        
        # maxi=float('-inf')

        # def finder(root,maxi):
        #     if not root:
        #         return 0

        #     left_height=find_height(root.left)
        #     right_height=find_height(root.right)

        #     current=left_height+right_height

        #     left=finder(root.left,maxi)
        #     right=finder(root.right,maxi)

        #     return max(current,left,right)
        
        # return finder(root,maxi)

        #Now trying optimal
        maxi=[0]
        def find_height(root,maxi):
            if not root:
                return 0

            lf=find_height(root.left,maxi)
            rt=find_height(root.right,maxi)

            maxi[0]=max(maxi[0],lf+rt)

            return max(lf,rt)+1

        find_height(root,maxi)
        return maxi[0]