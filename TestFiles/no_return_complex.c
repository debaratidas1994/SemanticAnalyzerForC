int func123(int a,int b,int c)
{
	if(c==1)
	{	
		if(a==1)
		{
			return c;
		}
		else
		{
			if(b==1)
			{
				return a;
			}
			else 
			{
				int x;
				int y;
				x=a+b;
				y=a*b;
				if(x<0)
				{
					return x;
				}
				else
				{
					if(x>10)
					{
						return y;
					}
				}	
			}
		}
	}


}
