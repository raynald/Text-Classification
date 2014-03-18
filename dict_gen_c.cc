#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

struct node {
    size_t word;
    size_t ind1;
    size_t ind2;
    node() {}
    node(size_t q, size_t p1, size_t p2) {
        word=q;ind1=p1;ind2=p2;
    }
};

string str;
string s[3500];
string r[3500];
int u,v;
int len;
int x;
node mat[3500*3500];
bool visit[3500];
bool vi[3500];
int fat[3500];
int son[3500];
bool z[3500];
double coei;
int ans;
int num;
int tmp;

bool cmp(const string &x, const string &y) {
    return x.length()>y.length();
}

bool operator<(const node &a, const node &b) {
    return a.word<b.word;
}

inline size_t min(size_t x, size_t y, size_t z) {
    if (x < y)
        return x < z ? x : z;
    else
        return y < z ? y : z;
}

size_t edit_distance(const string& A, const string& B) {
    size_t NA = A.size();
    size_t NB = B.size();

    vector< vector<size_t> > M(NA + 1, vector<size_t>(NB + 1));

    for (size_t a = 0; a <= NA; ++a)
        M[a][0] = a;

    for (size_t b = 0; b <= NB; ++b)
        M[0][b] = b;

    for (size_t a = 1; a <= NA; ++a)
        for (size_t b = 1; b <= NB; ++b) {
            size_t x = M[a-1][b] + 1;
            size_t y = M[a][b-1] + 1;
            size_t z = M[a-1][b-1] + (A[a-1] == B[b-1] ? 0 : 1);
            M[a][b] = min(x,y,z);
        }

    return M[A.size()][B.size()];
}

int father(int x) {
        return x==fat[x] ? x : father(fat[x]);
}

void joint(int x,int y) {
    int t1, t2;
    t1=father(x);
    t2=father(y);
    if(t1==t2) return;
    else {
        if(son[t1]>=son[t2]) {
            fat[t2]=t1;
            son[t1]+=son[t2];
        }
        else {
            fat[t1]=t2;
            son[t2]+=son[t1];
        }
    }
}

int main(int argc, char *argv[]) {
    freopen("dict_raw.txt","r",stdin);
    x=0;
    coei = atof(argv[1]);
    while(cin >> str) {
        x ++;
        s[x] = str;
        fat[x]=x;
        son[x]=1;
    }
    fclose(stdin);
    sort(s+1,s+x+1,cmp);
    memset(visit,0,sizeof(visit));
    num=0;
    for(int i=1;i<x;i++) {
        for(int j=i+1;j<=x;j++) {
            num++;
            mat[num]=node(edit_distance(s[i],s[j]),i,j);
        }
    }
    ans=0;
    for(int i=1;i<=num;i++) {
        u=mat[i].ind1;
        v=mat[i].ind2;
        if(mat[i].word<=coei*s[u].length()) {
            cout << s[u] << " " << s[v] << endl;
            joint(u,v);
        }
    }
    for(int i=1;i<=x;i++) {
        if(!visit[fat[i]]) {
            cout << s[fat[i]] << endl;
            visit[fat[i]]=1;
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

