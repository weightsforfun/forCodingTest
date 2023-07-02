import java.util.*;
class Solution {
    static int n;
    static int m;
    static int[][] move=new int[][] {{1,0},{-1,0},{0,1},{0,-1}};
    public int solution(String[] maps) {
        int answer = 0;
        n=maps.length;
        m=maps[0].length();
        int [] lever=new int[2];
        int [] start = new int[2];
        int [] end=new int[2];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(maps[i].charAt(j)=='S'){
                    start[0]=i;
                    start[1]=j;
                }
                else if(maps[i].charAt(j)=='L'){
                    lever[0]=i;
                    lever[1]=j;
                }
                else if(maps[i].charAt(j)=='E'){
                    end[0]=i;
                    end[1]=j;
                }
            }
        }
        
        Deque<int []> deq=new ArrayDeque<>();
        int [][] visited=new int[n][m];
        
        deq.offerLast(new int []{start[0],start[1],0});
        
        while(!deq.isEmpty()){
            int [] current=deq.pollFirst();
            int y=current[0];
            int x=current[1];
            int count=current[2];
            if(y==lever[0] && x==lever[1]){
                answer+=count;
                break;
            }
            for(int i=0;i<4;i++){
                int dy=move[i][0];
                int dx=move[i][1];
                int ny=y+dy;
                int nx=x+dx;
                if(ny>=0 && ny<n && nx>=0 && nx<m && maps[ny].charAt(nx)!='X'
                   && visited[ny][nx]==0){
                    deq.offerLast(new int[]{ny,nx,count+1});
                    visited[ny][nx]=1;
                }
            }
            
        }
        if(answer==0){
            return -1;
        }
        
        deq.clear();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                visited[i][j]=0;
            }
        }
        
        deq.offerLast(new int []{lever[0],lever[1],0});
        while(!deq.isEmpty()){
            int [] current=deq.pollFirst();
            int y=current[0];
            int x=current[1];
            int count=current[2];
            if(y==end[0] && x==end[1]){
                answer+=count;
                return answer;
            }
            for(int i=0;i<4;i++){
                int dy=move[i][0];
                int dx=move[i][1];
                int ny=y+dy;
                int nx=x+dx;
                if(ny>=0 && ny<n && nx>=0 && nx<m && maps[ny].charAt(nx)!='X'
                   && visited[ny][nx]==0){
                    deq.offerLast(new int[]{ny,nx,count+1});
                    visited[ny][nx]=1;
                }
            }
            
        }
        
        
        
        
        return -1;
    }
}