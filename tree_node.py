# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 
class TreeNode:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

    @staticmethod
    def print_tree(node, level=0):
        prefix = '  ' * level
        value = f": {node.value}" if node.value else ""
        print(f"{prefix}{node.type}{value}")
        for child in node.children:
            TreeNode.print_tree(child, level + 1)