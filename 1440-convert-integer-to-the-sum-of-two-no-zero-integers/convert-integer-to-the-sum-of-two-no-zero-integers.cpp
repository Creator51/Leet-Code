class Solution {
public:

    bool isNoZero(int num) {  
        while (num > 0) {
            if (num % 10 == 0) return false;
            num /= 10;
        }
        return true;
    }

    vector<int> getNoZeroIntegers(int n) {
        vector<int> x(2);
        int j;
        
        // FIrst i have kept 2 for Loops then to conpute J value is J=n-i SIMPLE LOGIC
        for(int i=1;i<n;i++){
             j=n-i;   
                if(i+j==n && isNoZero(i) && isNoZero(j)){
                x[0]=i;
                x[1]=j;
                return x;
                }
            
        }
       return x;
        
    }
};