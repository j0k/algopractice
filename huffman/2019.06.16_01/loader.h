#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using std::string;
using std::vector;

using std::cout;
using std::endl;

using std::ofstream;
using std::ifstream;

typedef vector<char> tcode01;

char* code2str(tcode01 code);
char  str2code(vector<char> chars);
char* chars2str(vector<char> chars);

class bitpacker {
public:
  tcode01 load(ifstream & stream);
  void save(tcode01 code, ofstream & stream);

  vector<char> load01(ifstream & stream); //code2str in the input
};

class Loader {
public:
  bitpacker packer;
  string fn_dict;

  ifstream fin;
  ofstream fout;

  tcode01 load();
  void save(tcode01 code);

  vector<char> load01();
};
