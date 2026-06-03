class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        n= len(landStartTime)
        m=len(waterStartTime)
        ans=float('inf')
        for i in range(n):
            for j in range(m):

                land = landStartTime[i] + landDuration[i]
                water = waterStartTime[j] + waterDuration[j]
                
                case1 = land + max(0,waterStartTime[j]-land) + waterDuration[j]
                case2= water + max(0,landStartTime[i]-water) + landDuration[i]

                ans=min(ans,case1,case2)


        return ans



           