class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n=nums.size();
        int longest=1;
        if(n==0)
        return 0;

        unordered_set<int> set;
        for(int i:nums){
            set.insert(i);
        }

        for(auto it:set){
            if(set.find(it - 1 )==set.end()){
                int count=1;
                int x=it;
                while(set.find(x+1)!=set.end()){
                    x+=1;
                    count+=1;
                }
                longest=max(longest,count);
            }


        }
        return longest;
    }
};