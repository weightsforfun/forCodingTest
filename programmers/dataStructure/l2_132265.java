import java.util.*;
class Solution {
    public int solution(int[] topping) {
        int answer = 0;

        HashMap<Integer,Integer> dic1 = new HashMap<Integer,Integer>();
        HashMap<Integer,Integer> dic2 = new HashMap<Integer,Integer>();        

        dic1.put(topping[0],1);

        for(int i=1;i<topping.length;i++){
            if(!dic2.containsKey(topping[i])){
                dic2.put(topping[i],1);    
            }
            else{
                dic2.put(topping[i],dic2.get(topping[i])+1);
            }
        }

        if(dic1.size()==dic2.size()){
            answer+=1;
        }

        for(int i=1;i<topping.length;i++){
            int topp=topping[i];

            if(!dic1.containsKey(topp)){
                dic1.put(topp,1);    
            }
            else{
                dic1.put(topp,dic2.get(topp)+1);
            }

            if(dic2.get(topp)==1){
                dic2.remove(topp);    
            }
            else{
                dic2.put(topp,dic2.get(topp)-1);
            }
            if(dic1.size()==dic2.size()){
                answer+=1;
            }
        }

        return answer;
    }
}