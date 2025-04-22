# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 
from parser import ParserLL1
from lexer import Lexer
import re
import sys

def numbers_only(s):
    return bool(re.fullmatch(r"\d+", s))

if len(sys.argv) < 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file) as f:
        examples = [line.strip() for line in f.readlines()]

    lexer = Lexer()
    parser = ParserLL1()

    for example in examples:
        try:
            if numbers_only(example): continue

            tokens = lexer.tokenize(example)
            parser.parse(tokens)

            print(f"valida")
        except SyntaxError:
            print(f"invalida")
            pass
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found")
    sys.exit(1)
except IOError:
    print(f"Error: Could not read file '{input_file}'")
    sys.exit(1)