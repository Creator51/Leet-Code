# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp=defaultdict(lambda :defaultdict(list))
        
        q=deque()
        q.append((root,0,0))

        while q:
            node,vertical,level=q.popleft()
            mp[vertical][level].append(node.val)
            if node.left:
                q.append((node.left,vertical-1,level+1))

            if node.right:
                q.append((node.right,vertical+1,level+1))

        ans=[]
        vals=mp.values()

        for verticals in sorted(mp.keys()):
            
            col=[]

            for levels in sorted(mp[verticals].keys()):
                col.extend(sorted(mp[verticals][levels]))

            ans.append(col)

        return ans