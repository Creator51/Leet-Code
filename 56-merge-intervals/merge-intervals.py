class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals.sort()
        ans=[]
        start=intervals[0][0]
        end=intervals[0][1]

        for i in range(1,len(intervals)):


            if intervals[i][0]<=end:
                end=max(intervals[i][1],end)
                continue
            else:
                ans.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        ans.append([start,end])
        return ans
        