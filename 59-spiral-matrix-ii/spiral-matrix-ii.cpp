class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;
        vector<vector<int>> ans(n, vector<int>(n, 0)); 
        int num = 1;

        while (top <= bottom && left <= right) {
            // Right
            for (int i = top; i <= right; i++) {
                ans[top][i] = num++;
            }
            top++;

            // Down
            for (int i = top; i <= bottom; i++) {
                ans[i][right] = num++;
            }
            right--;

            // Left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    ans[bottom][i] = num++;
                }
                bottom--;
            }

            // Up
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    ans[i][left] = num++;
                }
                left++;
            }
        }
        return ans;
    }
};
