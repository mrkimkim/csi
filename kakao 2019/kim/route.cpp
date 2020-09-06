#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool compare(const vector<int>& a, const vector<int>& b){
    if(a[1] == b[1]){
        return a[0] < b[0];
    }
    return a[1] > b[1];
}

void traverse(int y_cur, int low, int hi, int pre_or_post, vector<vector<vector<int>>>& xnode, vector<int>& pointer, vector<vector<int>>& ret){
    if(y_cur >= xnode.size() || pointer[y_cur] >= xnode[y_cur].size()){
        return;
    }
    if(low > xnode[y_cur][pointer[y_cur]][0] || hi < xnode[y_cur][pointer[y_cur]][0]){
        return;
    }
    int bound = xnode[y_cur][pointer[y_cur]][0];
    if(pre_or_post == 0){
        ret[pre_or_post].push_back(xnode[y_cur][pointer[y_cur]][1]);
        pointer[y_cur] += 1;
    }

    traverse(y_cur + 1, low, bound, pre_or_post, xnode, pointer, ret);
    traverse(y_cur + 1, bound, hi, pre_or_post, xnode, pointer, ret);

    if(pre_or_post == 1){
        ret[pre_or_post].push_back(xnode[y_cur][pointer[y_cur]][1]);
        pointer[y_cur] += 1;
    }

    return;

}

vector<vector<int>> solution(vector<vector<int>> nodeinfo) {
    for(int i = 0 ; i < nodeinfo.size(); ++i){
        nodeinfo[i].push_back(i+1);
    }
    sort(nodeinfo.begin(), nodeinfo.end(), compare);
    int prev = -1;
    vector<vector<vector<int>>> xnode;
    for(int i = 0 ; i < nodeinfo.size(); ++i){
        if(prev != nodeinfo[i][1]){
            prev = nodeinfo[i][1];
            xnode.push_back({{nodeinfo[i][0], nodeinfo[i][2]}});
        }
        else{
            xnode.back().push_back({nodeinfo[i][0], nodeinfo[i][2]});
        }
    }
    vector<int> pointer(xnode.size());
    vector<vector<int>> ret(2);
    traverse(0, INT_MIN, INT_MAX, 0, xnode, pointer, ret);
    
    fill(pointer.begin(), pointer.end(), 0);
    traverse(0, INT_MIN, INT_MAX, 1, xnode, pointer, ret);

    return ret;
}