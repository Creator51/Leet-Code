class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> ans;
        set<int> mp;
        for(int i=0;i<nums1.size();i++)
        mp.insert(nums1[i]);

        for(int i=0;i<nums2.size();i++)
        if(mp.find(nums2[i])!=mp.end())
        ans.insert(nums2[i]);

        return vector<int>(ans.begin(), ans.end());
        
    }
};