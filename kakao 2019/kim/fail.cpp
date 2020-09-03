#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<pair<double, int>> fail_rates(N);
    vector<int> counts(N+1);
    for(int i = 0 ; i < stages.size(); ++i){
        counts[stages[i]-1] += 1;
    }
    int sum = counts.back();
    for(int i = N-1 ; i >= 0 ; --i){
        sum += counts[i];
        if(sum == 0){
            fail_rates[i] = {(double)0.0 ,-(i+1)};
        }
        else{
            fail_rates[i] = {(double)counts[i] / sum ,-(i+1)};        
        }
    }
    sort(fail_rates.begin(), fail_rates.end(), greater<pair<double,int>>());
    vector<int> answer(N);
    for(int i = 0 ; i < N ; ++i){
        answer[i] = -fail_rates[i].second;
    }
    return answer;
}