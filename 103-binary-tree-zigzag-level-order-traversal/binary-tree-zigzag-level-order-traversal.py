# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        q=deque()
        q.append(root)
        flag=True

        if not root:
            return []

        while q:
            lev=[]
            for _ in range(len(q)):
                node=q.popleft()

                if node:
                    lev.append(node.val)

                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
                
            if lev:
                if flag:
                    ans.append(lev)
                else:
                    ans.append(lev[::-1])
                flag = not flag
        return ans
        