# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def make_parent(self,root,parents):
        q=deque()

        q.append(root)

        while q:
            node=q.popleft()

            if node.left:
                q.append(node.left)
                parents[node.left]=node

            if node.right:
                q.append(node.right)
                parents[node.right]=node

    def helper_node(self,root,k):
        q=deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node.val==k:
                return node
                break

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
        
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans=0
        q=deque()
        node=self.helper_node(root,start)
        q.append(node)
        visited=set()
        visited.add(node)
        parents={}
        self.make_parent(root,parents)
        while q:

            burnt=False

            for _ in range(len(q)):

                node=q.popleft()

                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                    burnt=True

                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                    burnt=True

                if node in parents and parents[node] not in visited:
                    q.append(parents[node])
                    visited.add(parents[node])
                    burnt=True

            if burnt:
                ans+=1

        return ans




        