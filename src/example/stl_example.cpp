#include <string>
#include <vector>
#include <map>

using namespace std;

string echo(string msg) {
    return msg;
}


vector<string> vector_int2str(vector<int> input) {
    vector<string> result;
    for (vector<int>::const_iterator it = input.begin(); it != input.end(); ++it) {
        result.push_back(to_string(*it));
    }
    return result;
}

map<int, string> reverse_map(map<string, int> input) {
    map<int, string> result;
    for (map<string, int>::const_iterator it = input.begin();
        it != input.end();
        ++it) {
        result[it->second] = it->first;
    }
    return result;
}