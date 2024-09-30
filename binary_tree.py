from graphviz import Digraph

class TreeNode:
    def __init__(self, final):
        self.final = final
        self.path = ''
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = TreeNode(False)

    def insert(self, value):
        actual_node = self.root
        father = None
        for i in range(len(value)):
            if value[i] == '0':
                if i == len(value) - 1:
                    if actual_node.right is None:
                        actual_node.right = TreeNode(True)
                        if father is None:
                            actual_node.right.path = '0'
                        else:
                            actual_node.right.path = actual_node.path + '0'
                    else:
                        actual_node.right.final = True
                else:
                    if actual_node.right is None:
                        actual_node.right = TreeNode(False)
                        if father is None:
                            actual_node.right.path = '0'
                        else:
                            actual_node.right.path = actual_node.path + '0'
                    father = actual_node
                    actual_node = actual_node.right
            
            elif value[i] == '1':
                if i == len(value) - 1:
                    if actual_node.left is None:
                        actual_node.left = TreeNode(True)
                        if father is None:
                            actual_node.left.path = '1'
                        else:
                            actual_node.left.path = actual_node.path + '1'
                    else:
                        actual_node.left.final = True
                else:
                    if actual_node.left is None:
                        actual_node.left = TreeNode(False)
                        if father is None:
                            actual_node.left.path = '1'
                        else:
                            actual_node.left.path = actual_node.path + '1'
                    father = actual_node
                    actual_node = actual_node.left

    def draw(self):
        dot = Digraph()

        def add_nodes_edges(node):
            if node.left:
                if node.left.final:
                    dot.node(str(node.left.path), color='red')
                else:
                    dot.node(str(node.left.path))
                dot.edge(str(node.path), str(node.left.path), label='1')
                add_nodes_edges(node.left)
            if node.right:
                if node.right.final:
                    dot.node(str(node.right.path), color='red')
                else:
                    dot.node(str(node.right.path))
                dot.edge(str(node.path), str(node.right.path), label='0')
                add_nodes_edges(node.right)
            
        add_nodes_edges(self.root)
        dot.render('binary_tree', view=True, format='png')