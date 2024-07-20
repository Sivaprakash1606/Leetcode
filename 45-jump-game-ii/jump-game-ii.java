class Solution {
    public int jump(int[] nums) {
        int left = 0;
        int right = 0;
        int result = 0;

        while (right < nums.length - 1) {
            int maxx = 0;
            for (int i = left; i <= right; i++) {
                if ((nums[i] + i) > maxx) {
                    maxx = nums[i] + i;
                }
            }
            left = right + 1;
            right = maxx;
            result++;
        }

        return result;
    }
}
