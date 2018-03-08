%module stl_example

%include "std_string.i"
%include "std_vector.i"
%include "std_map.i"

%{
#include "stl_example.hpp"
%}

namespace std {
  %template(StringVector) vector<string>;
  %template(IntVector) vector<int>;
  %template(Int2strMap) map<int, string>;
  %template(Str2intMap) map<string, int>;
}

%include "stl_example.hpp"
