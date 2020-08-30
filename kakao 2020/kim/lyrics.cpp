#include <bits/stdc++.h>
using namespace std;

/*
bool isMatched(string& w, string& q){
    if(w.size() != q.size()){
        return false;
    }
    for(int i = 0 ; i < w.size(); ++i){
        if(w[i] != q[i] && q[i] != '?'){
            return false;
        }
    }
    return true;
}

// naive solution
vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer(queries.size());
    for(int i = 0 ; i < queries.size(); ++i){
        int cnt = 0;
        for(int j = 0 ; j < words.size(); ++j){
            if(isMatched(words[j], queries[i])){
                ++cnt;
            }
        }
        answer[i] = cnt;
    }
    return answer;
}

*/

struct Trie{
    int cnt;
    vector<Trie*> children;
    Trie() : children(26,NULL), cnt(0) {}
    void insert(string& s, int pos){
        cnt += 1;
        if(s.size() - 1 == pos){
            return;
        }
        int next = s[pos+1] - 'a';
        if(children[next] == NULL){
            children[next] = new Trie();
        }
        children[next]->insert(s, pos+1);
        return;
    }
    int find(string& s, int pos){
        if(s.size() - 1 == pos){
            return 1;
        }
        if(s[pos+1] != '?'){
            int next = s[pos+1] - 'a';
            if(children[next] == NULL){
                return 0;
            }
            return children[next]->find(s, pos+1);
        }
        return cnt;
    }

};

// using Trie
vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer(queries.size());
    vector<Trie*> heads(10001);
    vector<Trie*> tails(10001);
    for(int i = 0 ; i < words.size() ; ++i){
        int n = words[i].size();
        if(heads[n] == NULL){
            heads[n] = new Trie();
            tails[n] = new Trie();
        }
        heads[n]->insert(words[i], -1);
        reverse(words[i].begin(), words[i].end());
        tails[n]->insert(words[i], -1);
    }
    for(int i = 0 ; i < queries.size(); ++i){
        if(heads[queries[i].size()] == NULL){
            answer[i] = 0;
        }
        else{
            if(queries[i][0] == '?'){
                reverse(queries[i].begin(), queries[i].end());
                answer[i] = tails[queries[i].size()]->find(queries[i],-1);
            }
            else{
                answer[i] = heads[queries[i].size()]->find(queries[i], -1);        
            }
        }
    }
    return answer;
}