import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        int n= numbers.length;
        int[] answer =new int [n];
        for(int i=0;i<n;i++){
            answer[i]=-1;
        }
        Deque<Integer> stack=new ArrayDeque<>();
        
        for(int i=0;i<n;i++){
            if(stack.isEmpty()){
                stack.addLast(i);
            }
            else{
                if(numbers[stack.peekLast()]>=numbers[i]){
                    stack.addLast(i);
                }
                else{
                    while(!stack.isEmpty() && numbers[stack.peekLast()]<numbers[i]){
                        int index=stack.removeLast();
                        answer[index]=numbers[i];
                    }
                    stack.addLast(i);
                }
            }
        }
        return answer;
    }
}