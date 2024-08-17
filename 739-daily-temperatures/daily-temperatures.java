class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack=new Stack<>();
        int result[]=new int[temperatures.length];
        for(int i=0;i<temperatures.length;i++){
            while(stack.size()>0 && temperatures[stack.peek()]<temperatures[i]){
                int j=stack.pop();
                result[j]=i-j;
            }
            stack.push(i);
        }
        return result;
        
    }
}