#include "btree.h"
using namespace std;
Node::Node(int value) {
  this->value = value;
  left = nullptr;
  right = nullptr;
}

void Node::add_node(Node* n) {
  if (n->value < this->value) {
    if (this->left == nullptr) {
      this->left = n;
    } else {
      this->left->add_node(n);
    }
  } else {
    if (this->right == nullptr) {
      this->right = n;
    } else {
      this->right->add_node(n);
    }
  }
}

Node* Node::search(int value) { 
    if (this->value == value ){
      return this;
    } else if(value < this->value  && this->left != nullptr){
      return this->left->search(value);
    } else if (value > this->value && this->right != nullptr) {
      return this->right->search(value);
    } else {
      return nullptr;
    }
}
void Node::visit() {
  if (this->left != nullptr) {
    this->left->visit();
  }
    cout << this->value << std::endl;
  if (this->right != nullptr) {
    this->right->visit();
  }
}

std::ostream& operator<<(std::ostream& os, const Node& n) {
  os << "Node( value=" << to_string(n.value) << ", left=" << (n.left ? to_string(n.left->value) : "nullptr") << ", right=" << (n.right ? to_string(n.right->value) : "nullptr") << ")" ;
  return os;
}
Tree::Tree() { this->root = nullptr; }

void Tree::add_value(int value) {
  if (this->root == nullptr) {
    this->root = new Node(value);
  } else {
    this->root->add_node(new Node(value));
  }
}

void Tree::traverse() { this->root->visit(); }
Node* Tree::search(int value) { 
    return this->root->search( value);
}