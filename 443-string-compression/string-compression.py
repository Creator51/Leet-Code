class Solution:
    def compress(self, chars: List[str]) -> int:

        count=1
        curr_char=chars[0]
        i=1
        indx=0
        while i<len(chars):
            if curr_char!=chars[i]:
                chars[indx]=curr_char
                indx+=1
                if count>1:
                    for digit in str(count):
                        chars[indx]=digit
                        indx+=1
                
                curr_char=chars[i]
                count=1
            else:
                count+=1
            i+=1

        chars[indx]=curr_char
        indx+=1

        if count>1:
            for digit in str(count):
                chars[indx]=digit
                indx+=1

        return indx


        



        
        