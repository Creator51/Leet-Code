class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]

        for a in asteroids:

            while st and a < 0 and st[-1] > 0 and st[-1] < -a:
                st.pop()

            if st and a<0 and st[-1]>0 and st[-1]==abs(a):
                st.pop()

            elif  not st or a >0 or st[-1] <0:
                st.append(a)

        return st