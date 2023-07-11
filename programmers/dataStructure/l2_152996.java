import java.util.*;
class Solution {
    public long solution(int[] weights) {
        long answer = 0;
        Long [] distinct =new Long[901];

        for(int i=0;i<901;i++){
            distinct[i]=0L;
        }

        Set<Integer> set=new HashSet<Integer>();

        for(int weight : weights){
            distinct[weight-100]+=1L;
            set.add(weight);
        }



        Integer[] setArray= set.toArray(new Integer[0]);
        Arrays.sort(setArray);

        for(int i=0;i<setArray.length;i++){
            for(int j=i;j<setArray.length;j++){
                if(setArray[i]*2==setArray[j] || 
                  setArray[i]*3==setArray[j]*2 ||
                  setArray[i]*4==setArray[j]*3){
                    answer+=(distinct[setArray[i]-100]*distinct[setArray[j]-100]);
                }
                else if(setArray[i]==setArray[j]){
                    answer+=(distinct[setArray[i]-100]*(distinct[setArray[i]-100]-1)/2);
                }
            }
        }



        return answer;
    }
}