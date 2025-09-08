#include <algorithm> 
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        //sort(nums.begin(), nums.end());
        int n=nums.size();
        int sum=(n*(n+1))/2;
        int real_sum=0;
        for(int i=0;i<nums.size();i++){
            real_sum+=nums[i];
        }
        return sum-real_sum;

        
    }
};