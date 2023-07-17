import java.util.*;
class Solution {
    public int solution(int storey) {
        int answer = Integer.MAX_VALUE;
        
        
        String str=Integer.toString(storey);
        int n=str.length();
        
        ArrayDeque<Integer []> deq=new ArrayDeque<>();
        
        deq.add(new Integer[] {n-1,0,0});
        
        while(!deq.isEmpty()){
            
            Integer [] temp=deq.removeFirst();
            int index=temp[0];
            int up=temp[1];
            int count=temp[2];
            
            if(index<0){
                if(up==1){
                    count+=1;
                }
                answer=Math.min(answer,count);
            }
            else{
                int num=str.charAt(index)-'0';
                if(up==1){
                    num+=1;
                }

                deq.addLast(new Integer[] {index-1,0,count+num});
                deq.addLast(new Integer[] {index-1,1,count+(10-num)});    
            }
            
        }
        
        return answer;
    }
}