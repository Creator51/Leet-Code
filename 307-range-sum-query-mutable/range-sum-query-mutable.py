class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.nums=nums
        self.tree=[0]*(4*self.n)

        self.build(1,0,self.n-1)

    def build(self,node,start,end):
        if start==end:
            self.tree[node]=self.nums[start]
            return 

        mid = (start+end)//2

        self.build(2*node,start,mid)
        self.build(2*node +1,mid+1,end)

        self.tree[node]=self.tree[2*node]+self.tree[2*node+1]

        

    def update_tree(self,node,start,end,index,val):
        if start==end:
            self.tree[node]=val
            return

        mid = (start +end)//2

        if index <= mid:
            #left side
            self.update_tree(2*node,start,mid,index,val)
        else:
            self.update_tree(2*node + 1,mid+1,end,index,val)

        self.tree[node]=self.tree[2*node]+self.tree[2*node+1]   

    def query(self,node,start,end,left,right):
        if left > end or right < start:
            return 0

        if left<=start and end<=right:
            return self.tree[node]

        mid= (start+end)//2

        return (self.query(2*node,start,mid,left,right) + self.query(2*node+1,mid+1,end,left,right))

        

    def update(self, index: int, val: int) -> None:
        self.update_tree(1,0,self.n-1,index,val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.query(1, 0, self.n - 1, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)