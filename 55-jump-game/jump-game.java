class Solution {
    public boolean canJump(int[] nums) {
        int s=nums[0];
        for(int i=1;i<nums.length;i++){
            if (s>0){
                s=s-1;
                int step=Math.max(s,nums[i]);
                s=step;
            }else{
                return false;
            }
        }
        return true;
    }
}