class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_num1={}
        for i in range(len(nums1)):
            hash_num1[nums1[i]]=i
        
        stack=[]
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                Index=hash_num1[val]
                res[Index] = cur

            if cur in hash_num1:
                stack.append(cur)
        return res

        