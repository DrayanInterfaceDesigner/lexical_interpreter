# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 
import re

class Lexer:
    TOKEN_TYPES = [
        ('OPERATORBINARIO', r'\\?(?:rightarrow|leftrightarrow|vee|wedge)'),
        ('OPERATORUNARIO', r'\\neg'),
        ('CONSTANTE', r'true|false'),
        ('PROPOSICAO', r'[a-z]'),
        ('ABREPAREN', r'\('),
        ('FECHAPAREN', r'\)'),
        ('ESPACO', r'\s+'),
        ('ERRO', r'.')
    ]

    def __init__(self):
        self.input = ''
        self.tokens = []
        self.pos = 0

    def reset(self):
        self.input = ''
        self.tokens = []
        self.pos = 0

    def tokenize(self, input_str):
        self.reset()
        self.input = input_str
        while self.pos < len(self.input):
            match = None
            for token_type, regex in self.TOKEN_TYPES:
                pattern = re.compile(regex)
                match = pattern.match(self.input, self.pos)
                if match:
                    value = match.group(0)
                    if token_type != 'ESPACO' and token_type != 'ERRO':
                        self.tokens.append((token_type, value))
                    self.pos = match.end()
                    break
            if not match:
                raise ValueError(f"Caractere inválido: {self.input[self.pos]}")
        
        return self.tokens