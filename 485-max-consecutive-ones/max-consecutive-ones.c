
int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int maxx=0;
    int one=0;
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]==1)
        {
            one+=1;
            if(one > maxx)
            {
                maxx=one;
            }
        }
        else
        {
            one=0;
        }
    }
    return maxx;
    
}