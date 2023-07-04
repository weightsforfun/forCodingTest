import java.util.*;
class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        int n=book_time.length;
        int[][] convert_time=new int[n][2];
        
        for(int i=0;i<n;i++){
            convert_time[i][0]=Integer.parseInt(book_time[i][0].substring(0,2))*60
                +Integer.parseInt(book_time[i][0].substring(3));
            convert_time[i][1]=Integer.parseInt(book_time[i][1].substring(0,2))*60
                +Integer.parseInt(book_time[i][1].substring(3));
        }
        
        Arrays.sort(convert_time,(t1,t2)->t1[0]-t2[0]);
        
        PriorityQueue<Integer> que=new PriorityQueue<>();
        
        for(int i=0;i<n;i++){
            if(que.isEmpty()){
                que.add(convert_time[i][1]);
                answer+=1;
            }
            else{
                int top=que.peek();
                if(top+10<=convert_time[i][0]){
                    que.remove();
                }
                else{
                    answer+=1;
                }
                que.add(convert_time[i][1]);
            }
        }
        
        
        return answer;
    }
}