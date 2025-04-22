# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 
from parser import ParserLL1
from lexer import Lexer
import re

def numbers_only(s):
    return bool(re.fullmatch(r"\d+", s))

with open('data/single/example.txt') as f:
    examples = [line.strip() for line in f.readlines()]

parser = ParserLL1()
lexer = Lexer()

for example in examples:
    try:
        if numbers_only(example): continue

        tokens = lexer.tokenize(example)
        parser.parse(tokens)

        print(f"valida")
    except SyntaxError:
        print(f"invalida")
        pass
