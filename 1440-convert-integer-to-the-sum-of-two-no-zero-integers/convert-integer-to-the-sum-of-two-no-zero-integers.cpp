class Solution {
public:

    bool isNoZero(int num) {   // \U0001f448 put this first
        while (num > 0) {
            if (num % 10 == 0) return false;
            num /= 10;
        }
        return true;
    }

    vector<int> getNoZeroIntegers(int n) {
        vector<int> x(2);

        

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i+j==n && isNoZero(i) && isNoZero(j)){
                x[0]=i;
                x[1]=j;
                return x;
                }
            }
        }
       return x;
        
    }
};