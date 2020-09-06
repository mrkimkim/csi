#include <bits/stdc++.h>

using namespace std;

bool isKey(int cur, int R, int C, vector<vector<string>>& relation){
    unordered_set<string> rows;
    for(int i = 0 ; i < R ; ++i){
        string s;
        for(int j = 0 ; j < C; ++j){
            if(cur & (1<<j)){
                s += relation[i][j];
            }
        }
        if(rows.count(s) > 0){
            return false;            
        }
        rows.insert(s);
    }
    return true;
}

void findKey(int cur, int pos, int R, int C, vector<vector<string>>& relation, vector<int>& cand){
    if(pos == C){
        return;
    }
    for(int i = pos ; i < C ; ++i){
        cur += (1 << i);
        if(isKey(cur, R, C, relation)){
            cand.push_back(cur);
        }
        else{
            findKey(cur, i+1, R, C, relation, cand);
        }
        cur -= (1 << i);
    }
    return;
}

int eraseDuplicate(vector<int>& cand){
    int ret = 0;
    for(int i = 0 ; i < cand.size(); ++i){
        bool isDuplicated = false;
        for(int j = i+1 ; j < cand.size(); ++j){
            int dup = cand[i] & cand[j];
            if(dup == cand[i] || dup == cand[j]){
                isDuplicated = true;
                break;
            }
        }
        if(isDuplicated == false){
            ret += 1;
        }
    }
    return ret;
}

int solution(vector<vector<string>> relation) {
    int R = relation.size();
    int C = relation[0].size();
    vector<int> cand;
    findKey(0, 0, R, C, relation, cand);
    int ret = eraseDuplicate(cand);
    return ret;
}