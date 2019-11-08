#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int main() {
    ll t;
    cin >> t;
    while(t--) {
        ll n ,m;
        cin >> n >> m;
        map <ll, ll> mp;
        vector <pair <ll, ll> > v;
        for(ll i = 0 ; i < m ; i++) {
            ll u , x;
            cin >> u >> x;
            mp[u]++;
            mp[x]++;
            v.push_back(make_pair(u,x));
        }

        if(m % 2 == 0) {
            cout << 1 << endl;
            for(ll i = 0 ; i < n ; i++) {
                cout << 1 << " ";
            }
            cout << endl;
        }
        else{
            ll flag = 0;
            ll val ;
            for(ll i = 1 ; i <= n ; i++) {
                if(mp[i] % 2 != 0){
                    flag = 1;
                    val = i;
                    break;
                }
            }
            // 2
            if(flag) {
                cout << 2 << endl;
                for(ll i = 1 ; i <= n ; i++) {
                    if(i == val) {
                        cout << 2 << " ";
                    }
                    else{
                        cout << 1 << " ";
                    }
                }
                cout << endl;
            }
            // 3
            else{
                cout << 3 << endl;
                ll count = 0;
                val = 0;
                for(ll i = 1 ; i <= n ; i++) {
                    if(mp[i] % 2 == 0 && mp[i] > 0) {
                        val = i;
                        break;
                    }
                }

                for(ll i = 0 ; i < m ; i++) {
                    ll p1,p2;
                    p1 = v[i].first;
                    p2 = v[i].second;
                    if(p1 == val || p2 == val) {
                        mp[p1] --;
                        mp[p2]--;
                    }
                }
                ll odd;
                for(ll i = 1 ; i <= n ; i++) {
                    if(mp[i] % 2 != 0) {
                        odd = i;
                        break;
                    }
                }

                for(ll i = 1 ; i <= n ; i++) {
                    if (i == val) {
                        cout << 1 << " ";
                    }
                    else if(i == odd) {
                        cout << 2 << " ";
                    }
                    else{
                        cout << 3 << " ";
                    }
                }
                cout << endl;
            }
        }
    }
    return 0;
}
