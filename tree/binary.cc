#include <iostream>
#include "btree.h"
using namespace std;

int main() { 
    Tree tree;
    tree.add_value(123);
    tree.add_value(12);
    tree.add_value(22);
    tree.add_value(23);
    tree.traverse();
    
}