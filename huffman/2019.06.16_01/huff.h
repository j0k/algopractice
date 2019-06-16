#include <string>

#include "loader.h"

using std::string;

Loader loader;

class Huffman {
  // two stages
  // load infile to create dict
  // load infie and dict to compress
  // -- save compressed
  // -- print buffered
  // load compressed and print output

  int status; // tmp variable

  void load_file(string fn);
  void create_dict();

  void save_dict(string fout);
  void load_dict(string fin);

  void compress(string fin, string dictfn, string fout); // compress file
  void print_buf_compress(string fin, string dict);

  void load_compressed(string dict, string fin);
};
