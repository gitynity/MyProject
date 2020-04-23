#include<fstream>
#include<string>
#include<unistd.h>
using namespace std;

int main()
{
		string data;
	
		ifstream input ("system_crasher.cpp");
		ofstream output ("system_crasher2.cpp");
		while(!input.eof())
		{
			
			getline(input , data);
			output<<data;
			output<<"\n";
			
		}
		input.close();
		output.close();
		
		//string cwd;
		//cwd = get_current_dir_name();
		system("cd $pwd");
		system("g++ system_crasher2.cpp");
		system("./a.out");
}
