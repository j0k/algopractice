#include "huff.h"

int main(int argc, char *argv[]){
  if (argc == 3){
    char * op1 = argv[1];
    char * fn  = argv[2];

    if (op1[0] == 'l' ){
      cout << "load" << endl;

      loader.fin.open(fn);
      tcode01 code = loader.load();
      cout << code2str(code);

      loader.fin.close();
    }

    if (op1[0] == '0' ){
      cout << "load" << endl;

      loader.fin.open(fn);
      vector<char> orig = loader.load01();
      cout << chars2str(orig);

      loader.fin.close();
    }
  }
  return 0;
}
