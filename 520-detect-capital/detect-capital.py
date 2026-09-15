class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capt=0
        for i in word:
            if  i.isupper():
                capt+=1

        if capt==len(word):
            return True
        elif capt==0 and len(word)>0:
            return True
        elif capt==1 and len(word)>0 and word[0].isupper():
            return True
        else:
            return False

        