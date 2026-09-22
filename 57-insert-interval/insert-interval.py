class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans=[]

        start=intervals[0][0]
        end=intervals[0][1]

        for i in range(1,len(intervals)):

            if intervals[i][0]<=end:
                end=max(end,intervals[i][1])
                continue
            else:
                ans.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        ans.append([start,end])
        return ans

        