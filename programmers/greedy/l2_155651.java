import java.util.*;
class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        int n=book_time.length;
        int[][] convert_time=new int[n][2];
        
        for(int i=0;i<n;i++){  // HH:MM -> 정수형태로 바꾸기
            convert_time[i][0]=Integer.parseInt(book_time[i][0].substring(0,2))*60
                +Integer.parseInt(book_time[i][0].substring(3));
            convert_time[i][1]=Integer.parseInt(book_time[i][1].substring(0,2))*60
                +Integer.parseInt(book_time[i][1].substring(3));
        }
        
        Arrays.sort(convert_time,(t1,t2)->t1[0]-t2[0]); //입실시간 기준으로 정렬
        
        PriorityQueue<Integer> que=new PriorityQueue<>();
        
        for(int i=0;i<n;i++){
            if(que.isEmpty()){   // 큐 비어있을 경우
                que.add(convert_time[i][1]);
                answer+=1;
            }
            else{
                int top=que.peek();
                if(top+10<=convert_time[i][0]){ // 방 추가 없이 입실 가능 (퇴실 + 청소시간 <입실)
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