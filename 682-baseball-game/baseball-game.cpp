class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> st;
        int ans=0;
        for(int i=0;i<operations.size();i++){
            if(operations[i]=="D"){
                st.push(st.top()*2);
            }else if( operations[i]=="C"){
                st.pop();
            }else if (operations[i]=="+"){
                int val1 = st.top();
                st.pop();
                int val2=st.top();
                st.push(val1);
                st.push(val1+val2);
            }else{
                st.push(stoi(operations[i]));
            }
        }
        while(!st.empty()){
            ans+=st.top();
            st.pop();

        }
        return ans;
    }
};