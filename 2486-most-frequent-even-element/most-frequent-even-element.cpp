class Solution {
public:
    int mostFrequentEven(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(int i:nums){
            if(i%2==0)
            mp[i]++;
        }
        int ans = -1, maxFreq = 0;
        for (auto &it : mp) {
            int num = it.first, freq = it.second;
            if (freq > maxFreq || (freq == maxFreq && num < ans)) {
                maxFreq = freq;
                ans = num;
            }
        }
        
        return ans;
        
    }
};