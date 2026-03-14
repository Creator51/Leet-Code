class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        #Consider smaller array
        if len(arr1)>len(arr2):
            arr1,arr2=arr2,arr1

        prefix_ans = set()

        for n in arr1:
            while n and n not in prefix_ans:
                prefix_ans.add(n)
                n = n // 10

        res =0 
        for i in arr2:
            while i!=0 and i not in prefix_ans:
                i=i//10 

            if i!=0:
                res=max(res, len(str(i)))
            
        return res




        