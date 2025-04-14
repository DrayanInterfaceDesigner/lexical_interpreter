# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 

from consts import *
from parser import Parser
from analyze import * 


parser: Parser = Parser()

parse_all_files('data/single', parser)
