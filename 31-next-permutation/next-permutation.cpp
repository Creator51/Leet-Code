class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int index=-1;
        int n=nums.size();
        // we are solving this problem in 3 parts
        // Find the break Point a[i]<a[i+1]
        for(int i=n-2;i>=0;i--){
            if(nums[i]<nums[i+1])
            {
                index=i;
                break;
            }
        }
        //if the index is -1 then the Given number is the largest So Reverse the number and Submit
        if(index==-1){
            reverse(nums.begin(),nums.end());
            return;
        }
        //Swap the Break point number with the next Greatest number from backside
        for(int i=n-1;i>=0;i--){
            if(nums[i]>nums[index]){
                swap(nums[i],nums[index]);
                break;
            }
        }
        //Now we got the Largest and The all Next Numbers should be Smallest
        reverse(nums.begin()+index+1,nums.end());

        
    }
};