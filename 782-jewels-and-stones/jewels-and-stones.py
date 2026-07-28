class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
    
        cnt=0

        for word in stones:
            if word in jewels:
                cnt+=1
        

        return cnt