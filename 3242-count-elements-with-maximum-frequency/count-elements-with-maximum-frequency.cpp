class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int,int> freq;
        int maxfreq=INT_MIN;
        for(int i=0;i<nums.size();i++){
            freq[nums[i]]++;
            maxfreq=max(maxfreq,freq[nums[i]]);
        }
        int ans = 0;
        for(auto &[num,f] : freq){
            if(f == maxfreq){
                ans+=f;
            }
        }
        return ans;
        
    }
};