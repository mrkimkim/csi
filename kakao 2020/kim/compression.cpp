#include <bits/stdc++.h>

using namespace std;

int solution(string s) {
    int answer = s.size();
    int half = s.size() / 2;
    for(int i = 1 ; i <= half; ++i){
        int tmp = 0;
        int count = 0;
        int idx = 0;
        string prev = "";
        while(idx + i <= s.size()){
            if(prev == s.substr(idx, i)){
                ++count;
            }
            else{
                if(count < 2){
                    tmp += prev.size();
                }
                else{
                    tmp += prev.size();
                    tmp += to_string(count).size();
                }
                prev = s.substr(idx, i);
                count = 1;
            }
            idx += i;
        }
        if(count >= 2){
            tmp += to_string(count).size();
        }
        tmp += prev.size();
        tmp += s.size() - idx;
        answer = min(answer, tmp);
    }
    return answer;
}