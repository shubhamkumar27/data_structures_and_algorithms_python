#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	ll t;
	cin t;
	cin>>t;
	while(t--){
		ll n,q;
		cin>>n>>q;
		ll arr[n-1] = {0};
		for(ll i=0;i<n-1;i++){
			cin>>arr[i];
		}
		while(q--){
			ll a,b;
			ll diff = abs(a - b);
			if(diff%2 == 1){
				ll mx = max(a,b);
				ll mn = min(a,b);
				mx--;
				mn--;
				cout<<mn<<" "<<mx<<endl;
				ll temp = arr[mn-1];
				cout<<temp<<endl;
				ll count = 0;
				for(ll i=mn;i<mx-1;i++){
					if(count%2 == 0){
						temp -= arr[i];
					}
					else{
						temp += arr[i];
					}
				}
				cout<<temp<<endl;
			}
			else{
				cout<<"UNKNOWN"<<endl;
			}
 		}
	}
	return 0;
}


