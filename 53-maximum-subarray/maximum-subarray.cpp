class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum=0;
        int max=INT_MIN;
        //Kadanes Algorithm
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];

            if(sum>max)
            max=sum;

            //If the Sum is going <0 Reset it as it has No Point
            if(sum<0)
            sum=0;

        }
        return max;
        
    }
};