class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total_gas=0;
        int total_cost=0;
        for (int i=0; i<gas.length;i++){
            total_gas+=gas[i];
            total_cost+=cost[i];
        }
        if (total_gas<total_cost){
            return -1;
        }
        int p=0;
        int s=0;
        for(int i=0; i<gas.length;i++){
            p+=gas[i];
            p-=cost[i];
            if(p<0){
                p=0;
                s=i+1;
            }
        }
        return s;
    }
}