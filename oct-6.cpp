#include <bits/stdc++.h>
#define ll long long int
using namespace std;

ll maxDigit(string s) {
    ll mx = 0;
    for(ll i = 0 ; i < s.size() ; i++) {
        if(s[i] >= '0' && s[i] <= '9') {
            ll v = s[i] - 48;
            mx = max(mx , v);
        }
        else{
            ll v = s[i] - 55;
            mx = max(mx , v);
        }
    }
    return mx;
}

ll calcnz (string s , ll b) {
    ll digit = 0;
    ll ans = 0;
    ll po = s.size() - 1;
    ll j = 0;
    for(ll i = po; i >= 0; i--) {
        if(s[i] >= '0' && s[i] <='9') {
            digit = s[i] - 48;
        }
        else{
            digit = s[i] - 65 + 10;
        }

        ll p = pow(b , j);
        j++;
        ans += (p * digit);
    }
    return ans;
}

ll calc (string s , ll b , ll start) {
    if(b < start) {
        return -1;
    }

    ll digit = 0;
    ll ans = 0;
    ll po = s.size() - 1;
    ll j = 0;

    for(ll i = po; i >= 0; i--) {
        if(s[i] >= '0' && s[i] <= '9') {
            digit = s[i] - 48;
        }
        else{
            digit = s[i] - 55;
        }

        ll p = pow(b , j);
        if(p < 0) {
            return -1;
        }
        j++;
        ans += (p * digit);
        if(ans > 1000000000000) {
            return -1;
        }
    }
    if(ans < 0) {
        return -1;
    }
    return ans;
}

int main(){
    ll t;
    cin >> t;
    while(t--) {
        ll n;
        cin >> n;
        ll temp = n;
        vector< pair <ll , string> > v;
        while (temp--) {
            ll base;
            string str;
            cin >> base >> str;
            v.push_back(make_pair(base , str));
        }

        ll sze  = v.size();
        ll flag = 0;

        vector < pair <ll , string> > non_zero;

        for (ll i = 0 ; i < sze; i++) {
            if(v[i].first != -1) {
                flag = 1;
                non_zero.push_back(make_pair(v[i].first , v[i].second));
            }
        }

        ll ans = 0;


        vector <ll> values;
        if(non_zero.size()) {
            for(ll i = 0; i < non_zero.size() ; i++) {
                ll inter = calcnz(non_zero[i].second , non_zero[i].first);
                values.push_back(inter);
            }
        }


        if(values.size() > 1) {
            ll real = 0;
            for(ll i = 1 ; i < values.size() ; i++) {
                if(values[i] != values[i-1]) {
                    real = 1;
                }
            }
            if(real) {
                cout << -1 << endl;
                continue;
            }
            else{
                ans = values[0];
            }
        }
        else{
            if(values.size()) {
                ans = values[0];
            }
        }

        if(flag) {
            ll arr[n][37];
            for(ll i = 0; i < n ; i++){
                for(ll j = 0 ; j < 37 ; j++) {
                    arr[i][j] = 0;
                }
            }

            for(ll i = 0 ; i < n ; i++) {
                ll start = maxDigit(v[i].second) + 1;
                for(ll j = 2 ; j <= 36 ; j++ ) {
                    ll store = 0;

                    string str = v[i].second;

                    store = calc (str , j , start);
                    arr[i][j] = store;
                    store = 0;
                }
            }


            ll breaker = 0;
            ll finalstatus = 0;
            for (ll i = 0; i < n ; i++) {
                breaker = 0;
                for (ll j = 2 ; j <= 36 ; j++) {
                    if(ans == arr[i][j]) {
                        breaker = 1;
                        break;
                    }
                }
                if(breaker == 1) {
                    continue;
                }
                else{
                    finalstatus = 1;
                    break;
                }
            }

            if(finalstatus) {
                cout << -1 << endl;
            }
            else{
                cout << ans << endl;
            }
        }
        else {
            ll arr[n][37];
            for(ll i = 0; i < n ; i++){
                for(ll j = 0 ; j < 37 ; j++) {
                    arr[i][j] = 0;
                }
            }

            for(ll i = 0 ; i < n ; i++) {
                ll start = maxDigit(v[i].second) + 1;
                for(ll j = 2 ; j <= 36 ; j++) {
                    ll store = 0;

                    string str = v[i].second;

                    store = calc(str , j , start);
                    arr[i][j] = store;

                    store = 0;
                }
            }

            // for(ll i = 0; i < n ; i++){
            //     for(ll j = 2 ; j <= 36 ; j++) {
            //         cout << arr[i][j] << " ";
            //     }
            //     cout<<endl;
            // }
            // cout << endl;

            unordered_map <ll , ll> x;
            unordered_map <ll , ll> final;
            unordered_map <ll ,ll> :: iterator itr;

            for(ll i = 2 ; i < 37 ; i++) {
                if(arr[0][i] != -1) {
                    x[arr[0][i]] = 1;
                }
            }

            if(x.size() == 0) {
                cout<< -1 <<endl;
                continue;
            }

            flag = 0;
            for(ll i = 1 ; i < n ; i++) {
                for(ll j = 2 ; j < 37 ; j++) {
                    if(arr[i][j] != -1) {
                        if(x[arr[i][j]]) {
                            final[arr[i][j]] = 1;
                        }
                    }
                }

                if(final.size() == 0) {
                    flag = 1;
                    break;
                }

                x.clear();
                for(itr = final.begin() ; itr != final.end() ; itr++) {
                    x[itr -> first] = 1;
                }
                final.clear();
            }


            if(flag) {
                cout << -1 << endl;
                continue;
            }

            ll mn = 1000000000000;
            map <ll,ll> mp;
            for(itr = x.begin() ; itr != x.end() ; itr++) {
                ll v = itr -> first;
                if(mn > v) {
                    mn = v;
                }
                mp[v] = 1;
            }
            // cout << mn << endl ;
            map <ll , ll> :: iterator it;
            for(it = mp.begin() ; it != mp.end() ; it++) {
                cout << it -> first << endl;
                break;
            }
        }
    }
    return 0;
}




// string s = v[index].second;
// ll b = v[index].first;
//
// ans = calc (s , b , 0);

// if(ans == -1) {
//     cout << -1 <<endl;
//     continue;
// }

// cout << ans <<endl;


// for(ll i = 0; i < n ; i++){
    //     for(ll j = 2 ; j <= 36 ; j++) {
        //         cout << arr[i][j] << " ";
        //     }
        //     cout<<endl;
        // }



                // for(ll i = 0 ; i < values.size() ; i++) {
                //     cout << values[i] << " ";
                // }
                // cout << endl;
