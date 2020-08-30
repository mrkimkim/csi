#include <bits/stdc++.h>
using namespace std;

vector<int> dmr = {1, -1, 0, 0};
vector<int> dmc = {0, 0, 1, -1};

bool reachDest(int r, int c, int dir, vector<vector<int>>& board){
    if(r == board.size() && c + 1 == board[0].size() && dir == 0){
        return true;
    }
    if(r == board.size() - 1 && c == board[0].size() && dir == 1){
        return true;
    }
    return false;
}

bool canGo(int r, int c, int dir, vector<vector<vector<int>>>& visited, vector<vector<int>>& board){
    if(r <= 0 || r > board.size() || c <= 0 || c > board[0].size()){
        return false;
    }
    if(visited[r][c][dir] != -1){
        return false;
    }
    if( (dir == 0 && c+1 > board[0].size()) || (dir == 1 && r+1 > board.size())){
        return false;
    }
    if(dir == 0 && board[r-1][c-1] == 0 && board[r-1][c] == 0){
        return true;
    }
    if(dir == 1 && board[r-1][c-1] == 0 && board[r][c-1] == 0){
        return true;
    }
    return false;    
}

void rotate(int r, int c, int ndir, int dist, vector<vector<vector<int>>>& visited, queue<vector<int>>& q){
    if(visited[r][c][ndir] == -1){
        q.push({r, c, ndir, dist+1});
        visited[r][c][ndir] = dist+1;
    }
    return;
}

bool pushQueue(vector<int>& here, vector<vector<vector<int>>>& visited, queue<vector<int>>& q, vector<vector<int>>& board){
    int r = here[0];
    int c = here[1];
    int dir = here[2];
    int dist = here[3];
    for(int i = 0 ; i < 4 ; ++i){
        if(canGo(r+dmr[i], c+dmc[i], dir, visited, board)){
            if(reachDest(r+dmr[i], c+dmc[i], dir, board)){
                return true;
            }
            q.push({r+dmr[i], c+dmc[i], dir, dist+1});
            visited[r+dmr[i]][c+dmc[i]][dir] = dist + 1;
            int ndir = (dir+1) % 2;
            if(dir == 0){
                if(dmr[i] == 1){
                    rotate(r, c, ndir, dist, visited, q);
                    rotate(r, c+1, ndir, dist, visited, q);
                }
                else if(dmr[i] == -1){
                    rotate(r-1, c, ndir, dist, visited, q);
                    rotate(r-1, c+1, ndir, dist, visited, q);
                }
            }
            else{
                if(dmc[i] == 1){
                    rotate(r, c, ndir, dist, visited, q);
                    rotate(r+1, c, ndir, dist, visited, q);
                }
                else if(dmc[i] == -1){
                    rotate(r, c-1, ndir, dist, visited, q);
                    rotate(r+1, c-1, ndir, dist, visited, q);
                }
            }
        }
    }
    
    return false;
}

int solution(vector<vector<int>> board) {
    queue<vector<int>> q;
    int R = board.size();
    int C = board[0].size();
    vector<vector<vector<int>>> visited(R+1, vector<vector<int>>(C+1, vector<int>(2, -1)));
    visited[1][1][0] = 0;
    q.push({1, 1, 0, 0});
    while(q.size() > 0){
        vector<int> here = q.front();
        q.pop();
        if(pushQueue(here, visited, q, board)){
            return here[3] + 1;
        }
    }
    return -1;
}