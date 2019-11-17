#include<iostream>
#include<fstream>
#include<cstring>
#include<string>
#include <regex> 
#include<sstream>
using namespace std;
int main()
{
	ofstream fout1("C:/Users/Joker/Desktop/title.txt");
	ofstream fout2("C:/Users/Joker/Desktop/body.txt");
	string filename_1 = "C:/Users/Joker/Desktop/vscode1/vscode";
	string filename_3 = ".txt";
	//ifstream fin("C:/Users/Joker/Desktop/vscode1/vscode2.txt");
	for (int i = 1; i <= 816; i++)
	{
		stringstream ss;
		string allTitle;
		string a;
		string filename_2;
		ss << i;
		ss >> filename_2;
		ifstream fin(filename_1 + filename_2 + filename_3);

		while (getline(fin, a)) {
			allTitle += a;
			allTitle += '\n';
		}
		//cout << allTitle << endl;
		smatch mat1;
		regex pattern1("\"title\":\\s\"(.*)\"");
		string::const_iterator start1 = allTitle.begin();
		string::const_iterator end1 = allTitle.end();
		while (regex_search(start1, end1, mat1, pattern1))
		{
			//cout << "1" << endl;
			string msg(mat1[1].first, mat1[1].second);
			fout1 << msg << endl;
			start1 = mat1[0].second;
		}
		smatch mat2;
		regex pattern2("\"body\":\\s\"(.*)\"");
		string::const_iterator start2 = allTitle.begin();
		string::const_iterator end2 = allTitle.end();
		while (regex_search(start2, end2, mat2, pattern2))
		{
			//cout << "1" << endl;
			string msg(mat2[1].first, mat2[1].second);
			fout2 << msg << endl;
			start2 = mat2[0].second;
		}
		fin.close();
	}
	//ofstream fout("C:/Users/Joker/Desktop/vscode1/vscode1.txt");
	 fout1.close(); fout2.close();
	return 0;
	
}