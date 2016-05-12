	#include <cmath>
	#include <cstdio>
	#include <vector>
	#include <iostream>
	#include <algorithm>
	using namespace std;
	
	int testcases=0, testcase_value, outside_sum=0, i=0, grand_array_index=0, grand_array[5000000];

	int howmany(int funcvar)
	{
		int sum=0;
	    for(int i=1; i< funcvar; i++)
	    {
	        for(int j=i; j<funcvar; j++)
	        {
	            for(int k=j; k<funcvar; k++)
	            {
	                if(i+j+k == funcvar  )
	                {
	                	if(i*i == j*j + k*k || j*j == i*i + k*k || k*k == i*i + j*j)
	                	{
	                	    //cout<<i<<" "<<j<<" "<<k<<" "<<endl;
	                        sum++;
	                	}
	                }
	            }
	        }
	    }
	    //cout<<sum<<endl;
	    //cout<<"inner sum "<<sum<<endl;
	    return sum;
	}

	int calculate_grand_array(int size)
	{
		int iter=0;
		if(grand_array_index > size)
			return grand_array_index;
		else
		{
			for(iter = grand_array_index+1; iter<= size; iter++)
			{
				grand_array[iter] = howmany(iter);
			}
			grand_array_index = iter;
	        return grand_array_index;
		}
	}


	int main() {
	     cin>>testcases;
	    while(testcases-->0)
	    {
	        cin>>testcase_value;
	        calculate_grand_array(testcase_value);
	        //cout<<grand_array_index;
	        //cout<<"a";
	    	for(int i=0; i<= testcase_value; i++)
	    	{

	            //cout<<grand_array[i];
	            //cout<<"B";
	    		if(grand_array[i] == 1)
	            {
	            	//cout<<grand_array[i];
	                outside_sum++;
	                //cout<<i<<"jhbj  "<<endl;
	            }
	    	}
	        cout<<outside_sum<<endl;
	        outside_sum=0;
	    }
	    return 0;
	}
