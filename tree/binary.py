class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def add_node(self, n):
    if n.value < self.value:
      if self.left == None:
        self.left = n
      else:
        self.left.add_node(n)

    else:
      if self.right == None:
        self.right = n
      else:
        self.right.add_node(n)

  def visit(self):
    if self.left:
      self.left.visit()
    print(self.value)
    if self.right:
      self.right.visit()

  def search(self, value):
    if self.value == value:
      return self

    elif value < self.value and self.left:
      return self.left.search(value)

    elif value > self.value and self.right:
      return self.right.search(value)

  def __repr__(self):
    return f"value={self.value}, left={self.left.value if self.left else None}, right={self.right.value if self.right else None}"


class Tree:
  def __init__(self):
    self.root = None

  def add_value(self, value):
    if not (self.root):
      self.root = Node(value)
    else:
      self.root.add_node(Node(value))

  def traverse(self):
    self.root.visit()

  def search(self, value):
    found = self.root.search(value)

    return found


tree = Tree()
tree.add_value(123)
tree.add_value(12)
tree.add_value(22)
tree.add_value(23)

tree.traverse()
print(tree.search(22))
