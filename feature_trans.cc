#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <fstream>

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
            size_t z = M[a-1][b-1] + (A[a-1] == B[b-1] ? 0 : 2);
            M[a][b] = min(x,y,z);
        }

    return M[A.size()][B.size()];
}

int main(int argc, char *argv[]) {
    string fea[100];
    int pos;
    int flen;
    ifstream infile;

    string ee="generated_dic"+string(argv[1])+".txt";
    freopen(ee.c_str(),"r",stdin);
    ans = 0;
    coei = atof(argv[2]);
    while(cin >> str && str.length()>0) {
        ans++;
        r[ans]=str;
    }
    fclose(stdin);
    infile.open("training.csv");
    string st = "training"+string(argv[1])+"-"+string(argv[2])+".vector";
    freopen(st.c_str(),"w",stdout);
    while(getline(infile,str) && str.length()>0) {
        std::transform(str.begin(), str.end(), str.begin(), ::tolower);
        len=str.find(",");
        if(len<0 || len > str.length()) len = str.length(); 
        str=str.substr(0,len);
        flen=0;
        while(1) {
            pos = str.find(" ");
            if(pos<0 || pos > str.length() ) pos = str.length();
            flen++;
            fea[flen]=str.substr(0,pos);
            if (pos==str.length()) break; else str=str.substr(pos+1,str.length());
        }
        memset(z,0,sizeof(z));
        for(int i=1;i<=ans;i++) {
            for(int j=1;j<=flen;j++) {
                if(r[i].length()>fea[j].length()) {
                    len=r[i].length()-fea[j].length(); 
                    tmp=fea[j].length();
                }
                else {
                    len=fea[j].length()-r[i].length();
                    tmp=r[i].length();
                }
                if(edit_distance(r[i],fea[j]) <  coei * r[i].length()) {
                    z[i]=1;
                    break;
                }
            }
        }
        for(int i=1;i<=ans;i++) {
            cout << z[i] << " " ;
        }
        cout << endl;
    }
    infile.close();
    fclose(stdout);
    infile.open("validation.csv");
    string tt = "validation"+string(argv[1])+"-"+string(argv[2])+".vector";
    freopen(tt.c_str(),"w",stdout);
    while(getline(infile,str) && str.length()>0) {
        std::transform(str.begin(), str.end(), str.begin(), ::tolower);
        len=str.find(",");
        if(len<0 || len > str.length()) len = str.length(); 
        str=str.substr(0,len);
        flen=0;
        while(1) {
            pos = str.find(" ");
            if(pos<0 || pos > str.length() ) pos = str.length();
            flen++;
            fea[flen]=str.substr(0,pos);
            if (pos==str.length()) break; else str=str.substr(pos+1,str.length());
        }
        memset(z,0,sizeof(z));
        for(int i=1;i<=ans;i++) {
            for(int j=1;j<=flen;j++) {
                if(r[i].length()>fea[j].length()) {
                    len=r[i].length()-fea[j].length(); 
                    tmp=fea[j].length();
                }
                else {
                    len=fea[j].length()-r[i].length();
                    tmp=r[i].length();
                }
                if(edit_distance(r[i],fea[j]) <  coei * r[i].length()) {
                    z[i]=1;
                    break;
                }
            }
        }
        for(int i=1;i<=ans;i++) {
            cout << z[i] << " " ;
        }
        cout << endl;
    }
    infile.close();
    fclose(stdout);
    infile.open("testing.csv");
    string ts = "testing"+string(argv[1])+"-"+string(argv[2])+".vector";
    freopen(ts.c_str(),"w",stdout);
    while(getline(infile,str) && str.length()>0) {
        std::transform(str.begin(), str.end(), str.begin(), ::tolower);
        len=str.find(",");
        if(len<0 || len > str.length()) len = str.length(); 
        str=str.substr(0,len);
        flen=0;
        while(1) {
            pos = str.find(" ");
            if(pos<0 || pos > str.length() ) pos = str.length();
            flen++;
            fea[flen]=str.substr(0,pos);
            if (pos==str.length()) break; else str=str.substr(pos+1,str.length());
        }
        memset(z,0,sizeof(z));
        for(int i=1;i<=ans;i++) {
            for(int j=1;j<=flen;j++) {
                if(r[i].length()>fea[j].length()) {
                    len=r[i].length()-fea[j].length(); 
                    tmp=fea[j].length();
                }
                else {
                    len=fea[j].length()-r[i].length();
                    tmp=r[i].length();
                }
                if(edit_distance(r[i],fea[j]) <  coei * r[i].length()) {
                    z[i]=1;
                    break;
                }
            }
        }
        for(int i=1;i<=ans;i++) {
            cout << z[i] << " " ;
        }
        cout << endl;
    }
    infile.close();
    fclose(stdout);
    return 0;
}

