# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]

        def helper(root,level,ans):

            if not root:
                return 

            if len(ans)==level:
                ans.append(root.val)

            helper(root.right,level+1,ans)
            helper(root.left,level+1,ans)

        helper(root,0,ans)
        return ans

            

            
        