import java.util.*;
class Solution {
    static int [][] visited;
    static int[][] move = {{1,0},{-1,0},{0,1},{0,-1}};
    static int n;
    static int m;
    static char [][] map;
    public int bfs(int y, int x){
        Deque<Integer[]> que = new ArrayDeque<>();
        que.addLast(new Integer[] {y,x});
        int foods=map[y][x]-'0';
        while(! que.isEmpty()){
            Integer [] current=que.removeFirst();

            for(int i=0;i<4;i++){
                int ny=current[0]+move[i][0];
                int nx=current[1]+move[i][1];

                if(ny>=0 && ny<n && nx>=0 && nx<m && visited[ny][nx]==0 && map[ny][nx]!='X'){
                    visited[ny][nx]=1;
                    foods+=map[ny][nx]-'0';
                    que.add(new Integer[] {ny,nx});
                }
            }
        }
        return foods;
    }

    public Integer[] solution(String[] maps) {

        n=maps.length;
        m=maps[0].length();
        List<Integer> answer = new ArrayList<>();
        visited = new int[n][m];
        map = new char[n][m];
        for(int i=0;i<n;i++){
            map[i]=maps[i].toCharArray();
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(visited[i][j]==0 && maps[i].charAt(j)!='X'){
                    visited[i][j]=1;
                    answer.add(bfs(i,j));
                }        
            }
        }
        if(answer.size()==0){
            return new Integer [] {-1};
        }

        Collections.sort(answer);
        return answer.toArray(new Integer[0]);
    }
}