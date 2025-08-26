class Solution {
public:
    int reverse(int x) {
        //int temp=x;
        long long rev=0,rem;
        while(x!=0){
            rem=x%10;
            rev=rev*10+rem;
            x=x/10;
        }
        if(x<0){
            rev=rev*(-1e9);
        }
        if (rev < INT_MIN || rev > INT_MAX) {
            return 0;
        }
        return rev;
    }
};
