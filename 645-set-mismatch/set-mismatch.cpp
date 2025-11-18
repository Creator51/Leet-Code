class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        unordered_map<int,int>m;
        for(int i : nums){
            m[i]++;
        }

        int ans1 = -1;
        int ans2 = 0;
        for(int i = 1 ; i <= nums.size();i++){
            if(m.find(i) == m.end()){
                ans2 = i;
            }
            if(m[i] == 2){
                ans1 = i;
            }
        }

        return {ans1,ans2};

    }
};