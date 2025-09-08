#include <algorithm> 
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int x;
        
        for(int i=0;i<nums.size();i++){
            if(i==nums[i]){

            }
            else{
                x=i;
                break;
            }
        }
        return x;
        
    }
};