class Solution {
    public int thirdMax(int[] nums) {
        double max1 = Double.NEGATIVE_INFINITY;
        double max2 = Double.NEGATIVE_INFINITY;
        double max3 = Double.NEGATIVE_INFINITY;
        for (int num : nums){
            if (num>max1){
                max3=max2;
                max2=max1;
                max1=num;
            }else if(num<max1 && num>max2){
                max3=max2;
                max2=num;
            }else if(num<max2 && num>max3){
                max3=num;
            }

        }
        if (max3 == Double.NEGATIVE_INFINITY) {
            return (int) max1;
        } else {
            return (int) max3;
        }
        
    }
}