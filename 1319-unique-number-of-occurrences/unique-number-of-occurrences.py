class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        dict1={}
        set1=set()

        for i in arr:
            dict1[i]=dict1.get(i,0)+1

        for i in dict1.keys():
            if dict1[i] in set1:
                return False
                
            else:
                set1.add(dict1[i])
                

        return True
        