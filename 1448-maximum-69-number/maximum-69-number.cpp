class Solution {
public:
    int maximum69Number (int num) {
        int maxx=0;
        string ans=to_string(num);
        for(int i=0;i<ans.length();i++)
        {
            int temp=ans[i];
            ans[i]='9';
            int num=stoi(ans);
            ans[i]=temp;
            maxx=max(maxx,num);
        }
        return maxx;
        
    }
};