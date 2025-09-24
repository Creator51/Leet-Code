class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<int> rows(matrix.size(), 0);
        vector<int> cols(matrix[0].size(), 0);

        //So Basically we are going to Locate the 0 in the matrix and SToring their Coloum
        // and rown so that In the next Iteration if rows || cols == 1 the full row and Coloum 
        // Becomes 0

        for(int i=0;i<matrix.size();i++)
        {
            for(int j=0;j<matrix[0].size();j++)

            {
                if(matrix[i][j]==0){
                    rows[i]=1;
                    cols[j]=1;
                }

            }
        }

        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++)
            {
                if(rows[i]==1 || cols[j]==1){
                    matrix[i][j]=0;
                }
            }
        }
        
    }
};