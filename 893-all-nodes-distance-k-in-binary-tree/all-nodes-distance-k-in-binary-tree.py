# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def mark_parent(self,root,parent_track):
        q=deque()
        q.append(root)

        while q:
            node=q.popleft()

            if node.left:
                q.append(node.left)
                parent_track[node.left]=node

            if node.right:
                q.append(node.right)
                parent_track[node.right]=node
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent_track={}
        self.mark_parent(root,parent_track)

        #visit BFS
        visited=set()
        q=deque()
        q=deque([target])
        visited.add(target)

        curr_lev=0

        while q:
            if curr_lev==k:
                break

            for _ in range(len(q)):

                node=q.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)

                if node in parent_track and parent_track[node] not in visited:
                    visited.add(parent_track[node])
                    q.append(parent_track[node])
            curr_lev+=1
        result = []

        while q:
            result.append(q.popleft().val)

        return result