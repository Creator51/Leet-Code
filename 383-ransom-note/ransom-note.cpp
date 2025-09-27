class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> mp;
        for(int i=0;i<magazine.size();i++){
            mp[magazine[i]]++;
        }
        for(int i=0;i<ransomNote.size();i++){
            char c = ransomNote[i];
            if (mp[c] > 0) {
                mp[c]--;
            }
            else
            return false;
        }
        return true;
        
    }
};