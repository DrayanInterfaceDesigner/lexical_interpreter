# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 
from tree_node import TreeNode

class ParserLL1:
    def __init__(self):
        self.reset()
        self.parse_table = {
            'S': {
                'PROPOSICAO': ['PROPOSICAO'],
                'CONSTANTE': ['CONSTANTE'],
                'OPERATORUNARIO': ['U'],
                'ABREPAREN': ['A']
            },
            'A': {
                'ABREPAREN': ['ABREPAREN', 'S', 'R']
            },
            'R': {
                'OPERATORBINARIO': ['OPERATORBINARIO', 'S', 'FECHAPAREN'],
                'FECHAPAREN': ['FECHAPAREN']
            },
            'U': {
                'OPERATORUNARIO': ['OPERATORUNARIO', 'S']
            }
        }

    def reset(self) -> None:
        self.tokens = None
        self.index = 0
        self.root = None

    def parse(self, tokens):
        self.reset()
        self.tokens = tokens
        self.root = TreeNode('S')
        stack = [('S', self.root)]

        while stack and self.index < len(self.tokens):
            current_token = self.tokens[self.index]
            current_type = current_token[0]
            symbol, node = stack.pop()

            if symbol in {'ABREPAREN', 'FECHAPAREN', 'OPERATORBINARIO',
                         'OPERATORUNARIO', 'PROPOSICAO', 'CONSTANTE'}:
                if symbol == current_type:
                    node.children.append(TreeNode(symbol, current_token[1]))
                    self.index += 1
                else:
                    raise SyntaxError(f"Esperado {symbol}, obteve {current_type}")
            else:
                if symbol not in self.parse_table:
                    raise SyntaxError(f"Símbolo inválido: {symbol}")
                
                productions = self.parse_table[symbol].get(current_type)
                if not productions:
                    expected = list(self.parse_table[symbol].keys())
                    raise SyntaxError(f"Erro em '{current_token[1]}'. Esperava {expected}")

                new_node = TreeNode(symbol)
                node.children.append(new_node)

                for elem in reversed(productions):
                    if elem in self.parse_table or elem in {
                        'ABREPAREN', 'FECHAPAREN', 'OPERATORBINARIO',
                        'OPERATORUNARIO', 'PROPOSICAO', 'CONSTANTE'
                    }:
                        stack.append((elem, new_node))
                    else:
                        raise ValueError(f"Produção inválida: {elem}")

        if self.index != len(self.tokens) or stack:
            remaining = len(self.tokens) - self.index
            raise SyntaxError(f"Entrada incompleta. Tokens restantes: {remaining}, Símbolos pendentes: {len(stack)}")

        return self.root


#     parser = ParserLL1()
    
#     input_tokens = [
#         ('ABREPAREN', '('), 
#         ('ABREPAREN', '('),
#         ('OPERATORUNARIO', '\\neg'),
#         ('CONSTANTE', 'true'),
#         ('FECHAPAREN', ')'),
#         ('OPERATORBINARIO', '\\rightarrow'),
#         ('CONSTANTE', 'false'),
#         ('FECHAPAREN', ')')
#     ]
    
#     try:
#         tree = parser.parse(input_tokens)
#         print("Árvore de análise:")
#         TreeNode.print_tree(tree)
#     except SyntaxError as e:
#         print(f"Erro de sintaxe: {e}")