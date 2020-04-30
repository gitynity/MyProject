#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

double cheating_detector(string a , string b)
{
    ifstream read1 , read2;
    vector<string> buffer1 , buffer2;

    read1.open(a);
    read2.open(b);

    int size1 = 0 , size2 = 0 , score = 0;

    string text1 , text2;

    while(!read1.eof())
    {					 
        read1>>text1;	
        buffer1.push_back(text1);
        size1++;
    }
    
    while(!read2.eof())
    {					
        read2>>text2;	
        buffer2.push_back(text2);
        size2++;
    }
    
    double smalllen = size1<size2?size1:size2;
    int temp = size1<size2?size1:size2;;

    for(auto i = 0;i<temp;i++)
    {
        if(buffer1.at(i) == buffer2.at(i))
            score++;
    }

    read1.close();
    read2.close();

    double result = 100*score/smalllen;

    return result ;
}

int main()
{
	vector<string> answers = {"RollNo.1" , "RollNo.2" , "RollNo.3" , "RollNo.4" , "RollNo.5" , "RollNo.6" , "RollNo.7"};
	
	for(size_t i = 0;i<answers.size();i++)
	{
		for(size_t j = i+1;j<answers.size();j++)
		{
			cout<<"The cheating score out of 100 for "<<answers.at(i)<<" and "<<answers.at(j)<<" is  "<<cheating_detector( answers.at(i) , answers.at(j) )<<"%\n";
		}
		cout<<endl;
	}
	
	return 0;
}
