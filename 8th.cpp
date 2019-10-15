#include <bits/stdc++.h>
#define ll long long
using namespace std;

unordered_map <ll, vector<pair<ll,ll> > > up;
unordered_map <ll, vector<ll> > t;
unordered_map <ll, vector<ll> > qu;
unordered_map <ll, ll> ans;
unordered_map <ll, ll> s;
vector <ll> ansindex;
ll mxh;
ll heights[500001];
ll visited[500001];
ll leafsize;
ll st[999999];

void update_ST(ll val , ll x){
	for(x += leafsize; x > 0; x >>= 1 ){
		st[x] += val;
	}
}

ll qST(ll x){
	ll ans=0;
	ll lss=leafsize;

	for(x += leafsize + 1; lss < x;  x >>= 1 , lss >>= 1){
		if(x&1){
			ans = ans + st[--x];
		}
		if(lss&1) {
			ans = ans + st[lss++];
		}
	}

	ll temp = 1;
	if(temp) {
		return ans;
	}
}

void dfs(ll node){

	ll val, ind;
	visited[node] = 1;
	bool is_leaf = true;

	vector <ll> child;

	if(t.find(node) != t.end()){
		for(auto currentnode : t[node]){
			if(visited[currentnode] == 0){
				child.push_back(currentnode);
			}
		}
	}

	if(child.size() > 0) {
		is_leaf = false;
	}

	if(up.find(node)!=up.end()){
		for(auto check: up[node]){
			s[check.first] += check.second;
			ll currentlevel = check.first + mxh+1;
			update_ST(check.second ,  currentlevel);
		}
	}

	if(qu.find(node) != qu.end()){
		for(ll i = 0 ; i < 100 ; i++) {
			ll x = 1;
		}
		for(auto index: qu[node]){
			if(!is_leaf){
				if(s.find(index - heights[node]) != s.end()){
					ans[index] = s[index-heights[node]];
				}
				else{
					ans[index]=0;
				}
			}
			else{
				ans[index] = qST(index+mxh-heights[node]+1);
			}
		}
	}



	for(auto x: child){
		if(visited[x] == 0){
			dfs(x);
		}
	}

	if(up.find(node)!=up.end()){
		for(auto x: up[node]){
			ll f = x.first;
			ll se = x.second;
			s[f] -= se;
			ll currentlevel = f;
			currentlevel += mxh;
			currentlevel++;
			update_ST(-se , currentlevel);
		}
	}

}

void ch(ll node, ll i){

	mxh = max(mxh , i);
	heights[node] = i;

	visited[node] = 1;

	if(t.find(node) != t.end()){
		for(auto nnode: t[node]){
			if(visited[nnode] != 1){
				ch(nnode , i+1);
			}
		}
	}

}

int main()
{

	ll n , q;
	cin >> n >> q;
	ll temp = n;
	temp --;

	for(ll i = 1 ; i <= n; i++) {
		heights[i] = 0;
		visited[i] = 0;
	}

	while(temp--) {
		ll u, v;
		cin >> u >> v;
		t[u].push_back(v);
		t[v].push_back(u);
	}


	ch(1, 0);

	for(ll i=1; i<=n; i++){
		ll val;
		cin >> val;
		temp = heights[i];
		up[i].push_back(make_pair( - temp - 1, val));
	}

	temp = q;
	ll i = 0;
	while(temp --) {
		string str;
		cin>>str;
		if(str[0] == '?'){
			ll node;
			cin >> node;
			ansindex.push_back(i);
			qu[node].push_back(i);
		}
		else{
			ll node = 0 ,  val = 0;
			cin >> node >> val;
			up[node].push_back(make_pair(i - heights[node] , val));
		}
		i++;
	}
	//
	// for(ll i = 0 ; i <= n ; i++) {
	// 	visited[i] = 0;
	// }

	leafsize = q;
	leafsize += mxh;
	leafsize ++;
	// st[2*leafsize];

	for(ll i = 1 ; i <= 2 * leafsize ; i++) {
		st[i] = 0;
	}

	dfs(1);

	for(ll i = 0; i < ansindex.size() ; i++){
		cout << ans[ansindex[i]] << endl;
	}

	return 0;
}
