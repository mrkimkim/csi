#include <bits/stdc++.h>
using namespace std;

// 기둥 1, 보 2
bool isStable(int x, int y, int t, vector<vector<int>>& matrix){
    int R = matrix.size();
    if(x < 0 || x >= R || y < 0 || y >= R){
        return true;
    }
    if(t == 0){
        if( (matrix[x][y] & 1) == 0){
            return true;
        }
        if( (y==0) || (y > 0 && (matrix[x][y-1] & 1)) || (x > 0 && (matrix[x-1][y] & 2)) || (matrix[x][y] & 2) ){
            return true;
        }
    }
    else{
        if( (matrix[x][y] & 2) == 0){
            return true;
        }
        if( (y > 0 && (matrix[x][y-1] & 1)) || (y > 0 && x + 1 < R && (matrix[x+1][y-1] & 1)) || (x > 0 && x + 1 < R && (matrix[x-1][y] & 2) && (matrix[x+1][y] & 2) ) ){
            return true;
        }
    }
    return false;
    
}

void remove_frame(vector<int>& frame, vector<vector<int>>& matrix){
    int x = frame[0];
    int y = frame[1];
    int t = frame[2];
    if(t == 0){
        matrix[x][y] -= 1;
        if( !(isStable(x, y+1, 0, matrix) && isStable(x, y+1, 1, matrix) && isStable(x-1, y+1, 1, matrix))){
            matrix[x][y] += 1;
        }
    }
    else{
        matrix[x][y] -= 2;
        if( !(isStable(x-1, y, 1, matrix) && isStable(x, y, 0, matrix) && isStable(x+1, y, 0, matrix) && isStable(x+1, y, 1, matrix))){
            matrix[x][y] += 2;
        }
    }
    return;
}

void create_frame(vector<int>& frame, vector<vector<int>>& matrix){
    int x = frame[0];
    int y = frame[1];
    int t = frame[2];
    matrix[x][y] += (t+1);
    if(!isStable(x, y, t, matrix)){
        matrix[x][y] -= (t+1);
    }
    return;    
}

vector<vector<int>> solution(int n, vector<vector<int>> build_frame) {
    vector<vector<int>> answer;
    vector<vector<int>> matrix(n+1, vector<int>(n+1));
    int C = build_frame.size();
    for(int i = 0 ; i < C; ++i){
        if(build_frame[i][3] == 0){
            remove_frame(build_frame[i], matrix);
        }
        else{
            create_frame(build_frame[i], matrix);
        }
    }
    
    for(int i = 0 ; i < n+1; ++i){
        for(int j = 0 ; j < n+1; ++j){
            // 기둥 - 1, 보 - 2
            if( (matrix[i][j] & 1)){
                answer.push_back({i, j, 0});
            }
            if( (matrix[i][j] & 2)){
                answer.push_back({i, j, 1});             
            }
        }
    }
    
    return answer;
}