#include<iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int people,age,count=0,temp;
        cin>>people>>age;
         while(people--){
            cin>>temp;
            if(temp>=age)
            count++;
         }
        cout<<count<<endl;
    }
    
}