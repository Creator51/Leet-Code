class Solution {
public:
    int maxFreqSum(string s) {
        unordered_map<char, int> mp;
        unordered_map<char,int> mp1;
        for(int i = 0; i < s.size(); i++) {
            if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
            mp[s[i]]++;
            else
            mp1[s[i]]++;              
        }
        int maxV = 0;
        for (auto &it : mp) {
            maxV = max(maxV, it.second);
        }

        
        int maxC = 0;
        for (auto &it : mp1) {
            maxC = max(maxC, it.second);
        }

        return maxV + maxC;
        

        return 0;
    }
};