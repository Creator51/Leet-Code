class Solution {
public:
    int maximum69Number (int num) {
        int st=0;
        string ans=to_string(num);
        for(int i=0;i<ans.length()-1;i++)
        {
            if(ans[i]=='6')
            break;

            st++;

        }
        ans[st]='9';
        return stoi(ans);
        
    }
};