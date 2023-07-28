import java.util.*;
class Solution {
    public int[] solution(int[] fees, String[] records) {

        int n=records.length;

        int base_time=fees[0];
        int base_fee=fees[1];
        int per_time=fees[2];
        int per_fee=fees[3];

        Map<String,String> dic= new HashMap<>();
        Map<String,Integer> final_dic=new HashMap<>();


        for(int i=0;i<n;i++){
            String[] splited= records[i].split(" ");
            String time=splited[0];
            String num=splited[1];
            if(dic.containsKey(num)){
                int start=timeConverter(dic.get(num));
                int end=timeConverter(time);

                dic.remove(num);
                if(final_dic.containsKey(num)){
                    final_dic.put(num,final_dic.get(num)+end-start);
                }
                else{
                    final_dic.put(num,end-start);
                }
            }
            else{
                dic.put(num,time);
            }
        }

        for(String key: dic.keySet()){
            int start=timeConverter(dic.get(key));
            int end=23*60+59;

            if(final_dic.containsKey(key)){
                    final_dic.put(key,final_dic.get(key)+end-start);
                }
                else{
                    final_dic.put(key,end-start);
                }
        }
        ArrayList<String> temp=new ArrayList<>();


        for(String key:final_dic.keySet()){
            temp.add(key);    
        }
        Collections.sort(temp);
        int[] answer = new int[temp.size()];
        int index=0;
        for(String t:temp){
            int fee=getFee(final_dic.get(t),base_fee,per_fee,base_time,per_time);
            answer[index]=fee;
            index++;
        }


        return answer;
    }
    int timeConverter(String time){
        String [] splited=time.split(":");
        String h=splited[0];
        String m=splited[1];
        return Integer.parseInt(h)*60 + Integer.parseInt(m);
    }


    int getFee(int time, int base_cost,int per_cost,int base_time,int per_time){
        if(time<=base_time){
            return base_cost;
        }
        int extra_cost=0;
        int extra_time=time-base_time;
        if((extra_time)%per_time==0){
            extra_cost=(extra_time)/per_time*per_cost;
        }
        else{
            extra_cost=(((extra_time)/(per_time))+1)*per_cost;
        }
        return base_cost+extra_cost;
    }
}