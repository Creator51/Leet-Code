class Solution {
public:
    int maxFreqSum(string s) {
        unordered_map<char, int> mp;
        unordered_map<char,int> mp1;
        int max_vovels=0,max_consonants=0;
        for(int i = 0; i < s.size(); i++) {
            if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u'){
            mp[s[i]]++;
            max_vovels=max(max_vovels,mp[s[i]]);
            }
            else{
            mp1[s[i]]++;
            max_consonants=max(max_consonants,mp1[s[i]]);
            }              
        }
        return max_vovels + max_consonants;

    }
};