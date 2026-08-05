# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        temp=[]

        def dfs(curr):
            if not curr:
                return 

            temp.append(str(curr.val))
            if not curr.right and not curr.left:
                ans.append("->".join(temp))
            else:
                dfs(curr.right)
                dfs(curr.left)

            temp.pop()

        dfs(root)

        return ans
        