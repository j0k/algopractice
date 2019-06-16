#include "huff.h"

Loader loader;

void Huffman::calc_weight(vector<char> text){
  for(int i = 0; i < text.size(); i++){
    char c = text[i];
    if (weights.count(c) > 0){
      weights[c] ++;
    } else {
      weights[c]  = 1;
    }
  }
}

void Huffman::print_weights(){
  for ( auto it = weights.begin(); it != weights.end(); it++ )
  {
    cout << it->first
         << ':'
         << it->second
         << std::endl ;
  }
}

void Huffman::create_dict(){
  djikstra_heap heap;
  int i = 0;

  for ( auto it = weights.begin(); it != weights.end(); it++ )
  {
    vector<int> v = {i++};
    symbol s{it->second, v};
    heap.push(s);

    tcode01 seq; // empty sequence
    pair_code code = {it->first, seq};
    codes.push_back(code);
  }

  if (heap.size() == 1){
    // only one symbol

  }
  while(heap.size() > 1){
    symbol lo = heap.top(); heap.pop();
    symbol hi = heap.top(); heap.pop();

    for (int i: lo.ref_code)
      codes[i].code.push_back(0);

    for (int i: hi.ref_code)
      codes[i].code.push_back(1);

    vector<int> vec;
    vec.reserve(lo.ref_code.size() + hi.ref_code.size());
    vec.insert(vec.end(), lo.ref_code.begin(), lo.ref_code.end());
    vec.insert(vec.end(), hi.ref_code.begin(), hi.ref_code.end());

    heap.push({lo.w + hi.w, vec});
  }

  //codesR = codes.copy();
  // copy(codes.begin(), codes.end(), back_inserter(codesR));
  //
  // FOR_IT(it,codesR){
  //  reverse((*it).code.begin(), (*it).code.end());
  // }
  //
  // FOR_IT(it,codes){
  //  reverse((*it).code.begin(),(*it).code.end());
  // }
}
