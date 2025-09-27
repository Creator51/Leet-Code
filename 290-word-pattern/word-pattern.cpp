class Solution {
public:
    bool wordPattern(string pattern, string s) {
        stringstream ss(s);
        string temp;
        vector<string> word;
        while(ss >> temp ){
            word.push_back(temp);
        }
        int m=pattern.size();
        int n=word.size();
        if(m!=n)
        return false;

        unordered_map<char,string> mp;
        unordered_set<string> s2;
        for(int i=0;i<pattern.size();i++){
            if((mp.find(pattern[i])==mp.end()) && (s2.find(word[i])==s2.end())){
            mp[pattern[i]]=word[i];
            s2.insert(word[i]);
            }
            else if(mp[pattern[i]]!=word[i]) {
                return false;

            }

        }
        return true;
        


        
    }
};