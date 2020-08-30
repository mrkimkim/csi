#include <bits/stdc++.h>
using namespace std;

bool isMatched(vector<vector<int>>& key, vector<vector<int>>& lock, int r, int c){
    int K = key.size();
    int R = lock.size();
    for(int i = 0 ; i < R; ++i){
        for(int j = 0 ; j < c ; ++j){
            if(lock[i][j] == 0){
                return false;
            }
        }
    }
    for(int i = 0 ; i < r; ++i){
        for(int j = 0 ; j < R ; ++j){
            if(lock[i][j] == 0){
                return false;
            }
        }
    }
    for(int i = r; i < R; ++i){
        for(int j = c; j < R; ++j){
            if(i < 0 || j < 0){
                continue;
            }
            if(i-r >= K || j-c >= K){
                if(lock[i][j] == 0){
                    return false;
                }
            }
            else if(key[i-r][j-c] == lock[i][j]){
                return false;
            }
        }
    }
    return true;
}

vector<vector<int>> rotate(vector<vector<int>> lock){
    int R = lock.size();
    vector<vector<int>> rotated_lock(R, vector<int>(R));
    for(int i = 0 ; i < R; ++i){
        for(int j = 0 ; j < R ; ++j){
            rotated_lock[i][j] = lock[R-1-j][i];
        }
    }
    return rotated_lock;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    int K = key.size();
    int L = lock.size();
    for(int t = 0 ; t < 4 ; ++t){
        for(int i = -K + 1; i < L; ++i){
            for(int j = -K + 1 ; j < L; ++j){
                if(isMatched(key, lock, i, j)){
                    return true;
                }
            }
        }
        key = rotate(key);
    }
    return false;
}