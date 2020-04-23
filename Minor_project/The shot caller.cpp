#include<iostream>
#include<string>
#include<unistd.h>
using namespace std;

int main()
{
		
		//string cwd;
		//cwd = get_current_dir_name();
		system("cd $pwd");
		system("g++ system_crasher.cpp");
		system("./a.out");
}
