class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
       int n=nums.size();
       vector<vector<int>> ans;
       // We will proceed with this Answer just Like the 3 Sum first we will sort the Array
       //We are USing 4 Pointer Approach(i,j,k,l)
       sort(nums.begin(),nums.end());
       for(int i=0;i<n;i++){
        if(i>0 && nums[i]==nums[i-1]) continue; //To skip the Dublicates of I
        for(int j=i+1;j<n;j++){
            if(j != i+1 && nums[j]==nums[j-1]) continue; // TO skip the Dublicates of J 
            int k=j+1;
            int l=n-1;
            while(k<l){
                long long sum=nums[i];
                sum+=nums[j];
                sum+=nums[k];
                sum+=nums[l];
                if(sum==target){
                    vector<int> temp={nums[i],nums[j],nums[k],nums[l]};
                    ans.push_back(temp);
                    k++,l--;
                    while(k < l && nums[k]==nums[k-1])k++;
                    while(k < l && nums[l]==nums[l+1])l--;
                    
                }else if(target > sum) 
                k++;
                else
                l--;
            }
            
        }
       }
       return ans;
        
    }
};