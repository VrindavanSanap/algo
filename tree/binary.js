function Node(value) {
  this.value = value
  this.left = null
  this.right = null
}

Node.prototype.visit = function () {
  if (this.left != null) {
   this.left.visit();
  }
  console.log(this.value);
  if (this.right != null) {
    this.right.visit();
  }
  return null;
}
Node.prototype.search = function (value) {
  if (this.value == value) {
    return this;
  } else if (value < this.value && this.left != null) {
    return this.left.search(value);
  } else if (value > this.value && this.right != null) {
    return this.right.search(value);
  }
}
Node.prototype.addNode = function (n) {

  if (n.value < this.value) {

    if (this.left == null) {
      this.left = n;
    } else {
      this.left.addNode(n)
    }
  } else {
    if (this.right == null) {
      this.right = n;
    } else {
      this.right.addNode(n)
    }
  }
}

function Tree() {
  this.root = null
}

Tree.prototype.addValue = function (value) {
  if (this.root == null) {
    this.root = new Node(value);
  } else {
    this.root.addNode(new Node(value));
  }
}
Tree.prototype.traverse = function (value) {
  this.root.visit();
}

Tree.prototype.search = function (value) {
  let found =   this.root.search(value);
  if (found != null){
    console.log(found)
  }
  return found
}
var tree;
tree = new Tree()
tree.addValue(123)
tree.addValue(12)
tree.addValue(22)
tree.addValue(23)
tree.traverse()

console.log(tree.search(23))
//console.log(tree.search(2))
