#include <bits/stdc++.h>

using namespace std;

int getMin(int state, int weak_pos, int dist_pos, vector<int>& weak, vector<int>& dist, vector<vector<vector<int>>>& dp, int n){
    if(dist_pos >= dist.size()){
        return INT_MAX;
    }
    if(dp[state][weak_pos][dist_pos] != -1){
        return dp[state][weak_pos][dist_pos];
    }
    int start = weak[weak_pos];
    int next_state = state;
    for(int i = weak_pos ; i < weak.size(); ++i){
        if(weak[i] <= start + dist[dist_pos]){
            next_state |= (1 << i);
        }
        else{
            break;
        }
    }
    if(start + dist[dist_pos] >= n){
        for(int i = 0 ; i < weak_pos; ++i){
            if(weak[i] <= ((start+dist[dist_pos]) % n)){
                next_state |= (1 << i);            
            }
            else{
                break;
            }
        }
    }
    if(next_state == (1<<((int)weak.size())) - 1){
        return dp[state][weak_pos][dist_pos] = 1;
    }
    int next = INT_MAX;
    for(int i = 0 ; i < weak.size() ; ++i){
        if( (next_state & (1 << i)) == 0 ){
            next = min(next, getMin(next_state, i, dist_pos+1, weak, dist, dp, n));
        }
    }
    if(next == INT_MAX){
        return dp[state][weak_pos][dist_pos] = INT_MAX;
    }
    return dp[state][weak_pos][dist_pos] = next + 1;
    
}

int solution(int n, vector<int> weak, vector<int> dist) {
    int answer = INT_MAX;
    sort(dist.begin(), dist.end(), greater<int>());
    int W = weak.size();
    int D = dist.size();
    if(dist[0] >= n){
        return 1;
    }
    vector<vector<vector<int>>> dp(1 << W, vector<vector<int>>(W, vector<int>(D, -1)));
    for(int i = 0 ; i < W; ++i){
        answer = min(answer, getMin(0, i, 0, weak, dist, dp, n));
    }
    if(answer == INT_MAX){
        return -1;
    }
    return answer;
}