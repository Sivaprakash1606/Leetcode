class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int maxx = 0;
        
        while (r < prices.length) {
            if (prices[r] > prices[l]) {
                int diff = prices[r] - prices[l];
                if (diff > maxx) {
                    maxx = diff;
                }
            } else {
                l = r;
            }
            r++;
        }
        
        return maxx;
    }
}
