class Solution:

    def helper(self,index,arr,target,anss,ds):

        if index == len(arr):
            if target == 0:
                anss.append(list(ds))
            return 

        if arr[index] <= target:
            ds.append(arr[index])
            self.helper(index,arr,target - arr[index],anss,ds)
            ds.pop()

        self.helper(index + 1 ,arr,target,anss,ds)
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ds=[]
        anss=[]
        self.helper(0,candidates,target,anss,ds)
        return anss


        