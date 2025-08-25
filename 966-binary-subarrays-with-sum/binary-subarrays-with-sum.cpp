class Solution {
public:
    // Helper function: count subarrays with sum <= goal
    int f(vector<int>& nums, int goal) {
        if (goal < 0) return 0; 
        int l = 0, r = 0;
        int n = nums.size();
        int s = 0, ans = 0;

        while (r < n) {
            s += nums[r];
            // shrink window if sum > goal
            while (s > goal) {
                s -= nums[l];
                l++;
            }

            // all subarrays ending at r with start from l..r are valid
            ans += (r - l + 1);
            r++;
        }
        return ans;
    }

    // Main function
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return f(nums, goal) - f(nums, goal - 1);
    }
};
