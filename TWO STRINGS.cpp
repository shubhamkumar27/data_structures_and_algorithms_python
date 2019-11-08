#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int flag=0;
		string a,b;
		cin>>a>>b;
		for(int i=0;i<a.length();i++)
		{
			for(int j=0;j<b.length();j++)
			{
				if(a[i]==b[i])
				{
					a[i]='*';
					b[j]='*';
					break;
				}
			}
		}
		
		for(int i=0;i<a.length();i++)
		{
			if(a[i]!=b[i])
			{
				flag=1;
				break;
			}
		}
		
		if(a.length()!=b.length())
		{
			cout<<"NO"<<endl;
		}
		
		if(flag==1)
		{
			cout<<"NO"<<endl;
		}
		else
		{
			cout<<"YES"<<endl;
		}
	}
	return 0;
}
