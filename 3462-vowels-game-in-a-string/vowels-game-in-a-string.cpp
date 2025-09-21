class Solution {
public:
    bool doesAliceWin(string s) {
        bool ans=false;
        for(int i=0;i<s.size();i++){
            if(s[i]=='a' || s[i]=='e' ||s[i]=='i' || s[i]=='o'|| s[i]=='u' )
            {
                ans=true;
                break;
            }
        }
        return ans;
        
    }
};