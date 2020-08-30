#include <string>
#include <vector>

using namespace std;

string makeCorrect(string& s){
    if(s.size() == 0){
        return s;
    }
    int count = 0;
    int u_last = 0;
    bool u_correct = true;
    for(int i = 0 ; i < s.size(); ++i){
        if(s[i] == '('){
            ++count;
        }
        else{
            --count;
        }
        if(count < 0){
            u_correct = false;
        }
        else if(count == 0){
            u_last = i;
            break;
        }
    }
    string v = s.substr(u_last+1);
    v = makeCorrect(v);
    string u;
    if(u_correct){
        u = s.substr(0, u_last+1);
        u += v;
    }
    else{
        u = "(";
        u += v;
        u += ")";
        for(int i = 1; i < u_last; ++i){
            if(s[i] == '('){
                u += ")";
            }
            else{
                u += "(";
            }
        }
    }
    return u;
    
}

string solution(string p) {
    string answer = makeCorrect(p);
    return answer;
}