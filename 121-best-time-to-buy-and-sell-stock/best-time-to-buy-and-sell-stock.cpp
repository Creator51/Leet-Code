class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minn=prices[0],profit=0;
        int cost=0;
        for(int i=1;i<prices.size();i++){
            cost=prices[i]-minn;
            profit=max(profit,cost);
            minn=min(minn,prices[i]);
            
        }
    return profit;
        
    }
};