import java.util.*;
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        int index=0;
        int now=1;
        ArrayDeque<Integer> stack= new ArrayDeque<>();
        while(index!=(order.length)){
            int item=order[index];
            if(now<item){
                stack.addLast(now);
                now+=1;
            }
            else if(now==item){
                index+=1;
                now+=1;
            }
            else{
                if(stack.getLast()==item){
                    stack.removeLast();
                    index+=1;
                }
                else{
                    break;
                }
            }
        }
        return index;
    }
}