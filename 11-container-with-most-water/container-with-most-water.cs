public class Solution {
    public int MaxArea(int[] height) {
        int left = 0, right = height.Length - 1, maxArea = 0;
        while (left < right) {
            maxArea = Math.Max(maxArea, (right - left) * Math.Min(height[left], height[right]));
            if (height[left] < height[right]) left++;
            else right--;
        }
        return maxArea;
    }
}