#include "loader.h"

char* code2str(tcode01 code){
  char * r_str = new char[code.size() * (1 + code.size()/8)];

  int c = 0;
  int j = 0;
  for(int i=0;i<code.size();i++){
    if (i>0 && (i%8 == 0)){
        r_str[j]=' ';j++;
      }
    r_str[j] = code[i] + (int)'0';
    j++;

  }

  return r_str;
}

// "10000000" means - 1
// "11111111" means - FF

char str2code(vector<char> chars){
  char c = 0;

  //  chars.size() <= 8

  for(int i=chars.size();i>=0;i--){
    if (chars[i] == '0') {
      c <<= 1;
    } else if (chars[i] == '1') {
      c = (c << 1) | 1;
    }
  }

  return c;

}


char* chars2str(vector<char> chars){
  char * r_str = new char[chars.size()];

  for(int i=0;i<chars.size();i++){
    r_str[i] = chars[i];
  }

  return r_str;
}

tcode01 bitpacker::load(ifstream & stream){
  tcode01 code;

  while(1){
    char raw  = 0;
    stream.read(&raw, sizeof(char));
    if (stream.eof())
      return code;
    // cout << raw;
    for(int i=0;i<8;i++){
      char mask = 1 << i;
      char bit  = !((mask & raw) == 0);
      code.push_back(bit);
    }
  }
  return code;
}

vector<char> bitpacker::load01(ifstream & stream){
  vector<char> allchars;
  vector<char> chars;

  int i = 0;
  while(1){
    char raw  = 0;
    stream.read(&raw, sizeof(char));
    if (stream.eof()){
      if (chars.size() > 0){
        allchars.push_back(str2code(chars));
        vector<char> freechars;
        chars = freechars;
      }
      return allchars;
    }


    if ((raw == '0') || (raw == '1')){
      chars.push_back(raw);
    }

    if (chars.size() == 8){
      allchars.push_back(str2code(chars));
      vector<char> freechars;
      chars = freechars;
    }

    // we read 01 stream

  }

  return allchars;
}

void bitpacker::save(tcode01 code, ofstream & stream){
  for(int i=0; i<code.size(); ){
    char raw=0;
    for(int j=i;(j<code.size()) && (j<i+8); j++){
        raw |= (code[j] << (j-i));
    }
    stream.write(&raw, sizeof(raw));
    i += 8;
  }
}

tcode01 Loader::load(){
  return packer.load(this->fin);
}

vector<char> Loader::load01(){
  return packer.load01(this->fin);
}

vector<char> Loader::load_orig(){
  vector<char> chars;
  while(1){
    char raw  = 0;
    fin.read(&raw, sizeof(char));
    chars.push_back(raw);
    if (fin.eof()){
        return chars;
    }
  }
  return chars;
}


void Loader::save(tcode01 code){
    packer.save(code, this->fout);
}
