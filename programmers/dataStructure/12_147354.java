import java.util.*;
class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        int n=col-1;
    
        Arrays.sort(data,(o1,o2) -> o1[n]==o2[n] ? o2[0]-o1[0]: o1[n]-o2[n]);
        
        for(int i=row_begin-1;i<row_end;i++){
            int temp=0;
            for(int num:data[i]){
                temp+=(num%(i+1));
            }
            answer=(answer ^ temp);
        }
        return answer;
    }
}