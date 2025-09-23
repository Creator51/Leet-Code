class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<int> v1,v2;
        string temp="";

        //Seperating them via '.'
        for(char c:version1){
            if(c=='.'){
                v1.push_back(stoi(temp));
                temp="";
            }
                else
                temp+=c;
            
        }
        v1.push_back(stoi(temp));

        temp="";
        for(char c:version2){
            if(c=='.'){
                v2.push_back(stoi(temp));
                temp="";
            }
                else
                temp+=c;
            
        }
        v2.push_back(stoi(temp));

        int len=max(v1.size(),v2.size());

        for(int i=0 ;i< len;i++){
            int n1 = i < v1.size() ? v1[i] : 0;
            int n2 = i < v2.size() ? v2[i] : 0;

            if(n1 > n2 )
            return 1;
            if(n1<n2)
            return -1;
        }
        return 0;

        
    }
};