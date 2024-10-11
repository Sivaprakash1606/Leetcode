class Solution {
    public int subarraySum(int[] nums, int k) {
        int result=0;
        Map<Integer,Integer> hm=new HashMap<>();
        int sum=0;
        for(int num:nums)
        {
            sum=sum+num;
            if(sum==k){
                result=result+1;
            }
            if(hm.containsKey(sum-k)){
                result=result+hm.get(sum-k);
            }
            if(hm.containsKey(sum)){
                hm.put(sum,hm.get(sum)+1);
            }else{
                hm.put(sum,1);
            }
        }return result;



    //     int result=0;
    //     for(int i=0;i<nums.length;i++)
    //     {
    //         int sum=0;
    //         for(int j=i;j<nums.length;j++)
    //         {
    //             sum=sum+nums[j];
    //             if(sum==k){
    //                 result++;
    //             }
    //         }
    //     }return result;
        
    }
}