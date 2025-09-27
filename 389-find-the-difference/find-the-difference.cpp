class Solution {
public:
    char findTheDifference(string s, string t) {
        unordered_map<char,int> mp;
        for(int i=0;i<t.size();i++){
            mp[t[i]]++;
        }

        for(int i=0;i<s.size();i++){
            if(mp.find(s[i])!=mp.end() && mp[s[i]]>0)
            mp[s[i]]--;
        }

        for (auto &p : mp) {
        if (p.second > 0) {
            return p.first ;       
        }
        }
        return '\0';
        
        
    }
};