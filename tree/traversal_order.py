from graphviz import Digraph

# Create a directed graph
dot = Digraph()

# Add nodes
dot.node('1', 'Root')
dot.node('2', 'Child 1')
dot.node('3', 'Child 2')
dot.node('4', 'Grandchild 1')
dot.node('5', 'Grandchild 2')
dot.node('6', 'Grandchild 3')
dot.node('7', 'Grandchild 4')

# Add edges (parent -> child)
dot.edges([
    ('1', '2'), ('1', '3'),
    ('2', '4'), ('2', '5'),
    ('3', '6'), ('3', '7')
])

# Render the graph
dot.render('tree_graph', format='png', cleanup=True)  # Saves as 'tree_graph.png'
dot.view()  # Opens the rendered image in the default viewer
