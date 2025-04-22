# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 
class Lexer:
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
        length = len(self.input)
        while self.pos < length:
            while self.pos < length and self.input[self.pos].isspace():
                self.pos += 1
            if self.pos >= length:
                break

            current_char = self.input[self.pos]

            if current_char == '(':
                self.tokens.append(('ABREPAREN', '('))
                self.pos += 1
            elif current_char == ')':
                self.tokens.append(('FECHAPAREN', ')'))
                self.pos += 1
            elif current_char == '\\':
                start = self.pos
                self.pos += 1 
                while self.pos < length and not self.input[self.pos].isspace() and self.input[self.pos] not in '()':
                    self.pos += 1
                operator = self.input[start:self.pos]
                if operator == r'\neg':
                    self.tokens.append(('OPERATORUNARIO', operator))
                elif operator in (r'\rightarrow', r'\leftrightarrow', r'\vee', r'\wedge'):
                    self.tokens.append(('OPERATORBINARIO', operator))
                else:
                    raise ValueError(f"Operador inválido: {operator}")
            elif current_char.isalpha():
                if current_char == 't':
                    if (self.pos + 3 < length and
                        self.input[self.pos+1:self.pos+4] == 'rue' and
                        (self.pos +4 == length or self.input[self.pos+4].isspace() or self.input[self.pos+4] in '()')):
                        self.tokens.append(('CONSTANTE', 'true'))
                        self.pos += 4
                    else:
                        self.tokens.append(('PROPOSICAO', current_char))
                        self.pos += 1
                elif current_char == 'f':
                    if (self.pos + 4 < length and
                        self.input[self.pos+1:self.pos+5] == 'alse' and
                        (self.pos +5 == length or self.input[self.pos+5].isspace() or self.input[self.pos+5] in '()')):
                        self.tokens.append(('CONSTANTE', 'false'))
                        self.pos += 5
                    else:
                        self.tokens.append(('PROPOSICAO', current_char))
                        self.pos += 1
                else:
                    self.tokens.append(('PROPOSICAO', current_char))
                    self.pos += 1
            else:
                raise ValueError(f"Caractere inválido: {current_char}")
        return self.tokens