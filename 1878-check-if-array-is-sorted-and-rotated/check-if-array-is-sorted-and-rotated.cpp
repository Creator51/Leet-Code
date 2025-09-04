class Solution {
public:
    bool check(vector<int>& nums) {
        int drop=0;
        for(int i=1;i<nums.size();i++){
            //THe Main Logic is Drop should be <= 1 
            if(nums[i]<nums[i-1])
            drop++; //Sorted Array Contains Only 1 Drop
        }
        //If the Array is Not Correctly there will be an Drop
        if(nums[nums.size()-1]>nums[0])
        drop++;

        return drop<=1;

    }
};