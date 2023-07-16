import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        int answer = 0;
        Deque<Integer[]> deq= new ArrayDeque<>();
        deq.addLast(new Integer[] {x,0});
        int visited[]=new int[1000001];
        visited[x]=1;

        while(! deq.isEmpty()){
            Integer[] now =deq.removeFirst();
            Integer num=now[0];
            Integer count=now[1];
            if(num == y){
                return count; 
            }
            if(num*2<=y && visited[num*2]==0 ){
                deq.addLast(new Integer[]{num*2,count+1});
                visited[num*2]=1;
            }
            if( num*3<=y && visited[num*3]==0 ){
                deq.addLast(new Integer[]{num*3,count+1});
                visited[num*3]=1;
            } 
            if(num+n<=y && visited[num+n]==0  ){
                deq.addLast(new Integer[]{num+n,count+1});
                visited[num+n]=1;
            } 
        }
        return -1;
    }
}
