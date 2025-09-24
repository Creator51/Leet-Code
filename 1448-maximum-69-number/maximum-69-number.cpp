class Solution {
public:
    int maximum69Number (int num) {
        string n = to_string(num);
        int st=0;
        int end=n.length()-1;
        while(st< end && n[st] == '9'){
            st++;
        }
        n[st]='9';
        return stoi(n);
    }
};