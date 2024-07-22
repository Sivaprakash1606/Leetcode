class Solution {
    public int addDigits(int num) {
        String string=String.valueOf(num);
        if (string.length()==1){
            return num;
        }       
        int summ=0;
        for(char c:string.toCharArray()){
            summ=summ+Character.getNumericValue(c);
        }
        return addDigits(summ);
        }
}