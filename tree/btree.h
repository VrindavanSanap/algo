#ifndef TREE_H
#define TREE_H

#include <iostream>

class Node {
 public:
  int value;
  Node* left;
  Node* right;
  Node(int value);
  void add_node(Node* n);
  void visit();
  Node* search(int value);
  friend std::ostream& operator<<(std::ostream& os, const Node& n);
};

class Tree {
 public:
  Node* root;
  Tree();
  void add_value(int value);
  void traverse();
  Node* search(int value);
};

#endif /* TREE_H */
