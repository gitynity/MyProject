#include<iostream>
#include<unistd.h>
int main()
{
	//int i=10;
	while(true)
	{
		fork();
		system("ping 127.0.0.1");
	}
return 0;
}
