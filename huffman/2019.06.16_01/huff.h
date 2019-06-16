#pragma once
#include <string>
#include <map>
#include <queue>
#include <functional>

#include "loader.h"

using std::string;
using std::map;
using std::priority_queue;

using std::cout;
using std::endl;

using namespace std;

struct pair_code{
  char letter; // first
  tcode01 code;
};

typedef vector<pair_code> huffman_codes;

struct symbol {
    int   w;
    vector<int> ref_code;
    bool operator> (const symbol &ref) const {return w > ref.w;}
};

typedef priority_queue<symbol, std::deque<symbol>, std::greater<symbol> > djikstra_heap;

class Huffman {
public:
  // two stages
  // load infile to create dict
  // load infie and dict to compress
  // -- save compressed
  // -- print buffered
  // load compressed and print output

  map<char,int> weights;
  huffman_codes codes;

  void calc_weight(vector<char> text);
  void print_weights();

  void load_file(string fn);
  void create_dict();

  void save_dict(string fout);
  void load_dict(string fin);

  void compress(string fin, string dictfn, string fout); // compress file
  void print_buf_compress(string fin, string dict);

  void load_compressed(string dict, string fin);
};
