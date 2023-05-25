#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
static int temp=0;
int sili(string aa, char a,int high, int low){
    int si=high;
    for(int i=high+1;i<=low;i++){
        if(aa[i]>a && aa[i]<aa[si]){
            si=i;
        }
    }
    return si;
}
void permute(string s){
    int a;
    a=s.length();
    sort(s.begin(),s.end());
    bool ab=false;
    int i;
    while(!ab){
        cout<<s<<endl;
        temp++;
        for(i=a-2;i>=0;i--){ //abcd
            if(s[i]<s[i+1])
            break;
        }
        if(i== -1){
        ab=true;
        cout<<temp;}
        else{
            int k=sili(s,s[i],i+1,a-1);
            swap(s[i],s[k]);
            sort(s.begin()+i+1,s.end());

        }
        }
        }
int main(){
    string abc;
    cin>>abc;
    cout<<"............";
    permute(abc);
}