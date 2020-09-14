#include<bits/stdc++.h>

using namespace std;

long long a[1000005],t[1000005];
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n,k;
    cin>>n>>k;
    for(int i=1;i<=n;i++){
        cin>>a[i];
    }
    for(int i=1;i<=n;i++){
        cin>>t[i];
    }
    long long result=0;
    a[0]=0;
    for(int i=1;i<=n;i++){
        if(t[i]==0) a[i]+=a[i-1];
        else {
            result+=a[i];
            a[i]=a[i-1];
        }
    }
    long long re=0;
    for(int i=1;i<=n-k+1;i++){
        re=max(re,a[i+k-1]-a[i-1]);
    }
    cout<<re+result<<endl;
return 0;
}