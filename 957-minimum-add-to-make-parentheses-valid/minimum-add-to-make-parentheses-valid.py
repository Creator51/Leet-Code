class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt_o,cnt_c=0,0

        if not s:
            return 0
        # req=0 
        # i=0
        # while i < len(s):
            
        #     if s[i]=='(':
        #         req+=1
        #         if i<len(s)-1 and s[i+1]==')':
        #             req-=1
        #             i=i+1
        #     elif s[i]==')':
        #         if req>0:
        #             req-=1
        #         else:
        #             req+=1
                
        #     i+=1

        # return req
        st=[]

        for i in range(len(s)):
            if s[i]=='(':
                st.append(s[i])

            elif s[i]==')' and st and st[-1]=='(':
                st.pop()

            else:
                st.append(s[i])            

        return len(st)

            