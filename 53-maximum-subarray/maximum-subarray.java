class Solution {
    public int maxSubArray(int[] nums) {
        int m=nums[0];
        int c=0;
        for(int i:nums){
            if (c<0){
                c=0;
            }
            c=c+i;
            if (c>m){
                m=c;
            }
        }
        return m; 
    }
}