#include <iostream>
#include <vector>

using namespace std;

class character{
    private:
        int x;
        int y;
        int drc;
    public:
        character(int i,int j,int k){
            x=i;
            y=j;
            drc=k;
        } 
        void set_loc(int i,int j){
            x=i;
            y=j;
        }
        void set_drc(int direction){
            drc=direction;
        }
        int get_x(){
            return x;
        }
        int get_y(){
            return y;
        }
        void turn_left(){
            drc--;
            if(drc==-1)
                drc = 3;
        }
        int get_drc(){
            return drc;
        }
};

int main(){
    // map size
    int N,M;
    cin >> N;
    cin >> M;
    cin.ignore();

    int n,m;    // character location
    int drc;    // character direction
    cin >> n;
    cin >> m;
    cin >> drc;
    
    character cha(n,m,drc);

    int map[N][M];
    int recent[N][M];
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> map[i][j];
            recent[i][j] = map[i][j];
        }
    }

    int dx[4] = {0,1,0,-1};
    int dy[4] = {-1,0,1,0};
    
    int turn_cnt = 0;
    int move_cnt = 1;
    while(1){
        //왼쪽으로 회전
        cha.turn_left();
        int tmp_x = cha.get_x() + dx[cha.get_drc()];
        int tmp_y = cha.get_y() + dy[cha.get_drc()];
        //회전 후 바라보는 방향이 바다가 아니고 가본곳도 아니라면 이동
        if(map[tmp_x][tmp_y] == 0 && recent[tmp_x][tmp_y] == 0){
            cha.set_loc(tmp_x, tmp_y);
            recent[tmp_x][tmp_y] = 1;
            move_cnt++;
        }
            
        //회전 후 바라보는 방향이 바다이거나 가본곳이라면
        else
            turn_cnt++;
        
        //네 방향 모두 갈 수 없으면 
        if(turn_cnt == 4){
            tmp_x = cha.get_x() - dx[cha.get_drc()];
            tmp_y = cha.get_y() - dy[cha.get_drc()];

            //뒤로 갈 수 있으면 이동
            if(map[tmp_x][tmp_y] == 0)
                cha.set_loc(tmp_x, tmp_y);
            else
                break;
            turn_cnt = 0;
        }
    }
    
    cout << move_cnt << endl;

    return 0;
}

