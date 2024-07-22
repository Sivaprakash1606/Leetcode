class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        for(int i=0;i<heights.length-1;i++){
            for(int j=0;j<heights.length-1;j++){
                if(heights[j]>heights[j+1]){
                    continue;
                }
                else{
                    int tempHeight = heights[j];
                    heights[j]=heights[j+1];
                    heights[j+1]=tempHeight;

                    String tempNames=names[j];
                    names[j]=names[j+1];
                    names[j+1]=tempNames;
                }
            }
        }
        return names;
    }
}