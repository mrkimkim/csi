#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int solution(vector<int> food_times, ll k) {
    map<ll, ll> m;
    ll total = 0;
    for(int i = 0 ; i < food_times.size() ; ++i){
        m[food_times[i]] += 1;
        total += food_times[i];
    }
    if(total <= k){
        return -1;
    }

    ll left = food_times.size();
    ll eaten = 0;
    ll prev = 0;
    ll cur = 0;
    for(auto it = m.begin(); it != m.end() ; ++it){
        cur = it->first;
        eaten += left * (cur - prev);
        if(eaten >= k+1){
            eaten -= left * (cur - prev);
            break;
        }
        left -= it->second;
        prev = cur;
    }

    ll mod = (k+1 - eaten) % left;
    if(mod == 0){
        mod = left;
    }
    ll ret = 0;

    for(int i = 0 ; i < food_times.size(); ++i){
        if(cur > food_times[i]){
            continue;
        }
        mod -= 1;
        if(mod == 0){
            ret = i+1;
            break;
        }
    }

    return ret;

}