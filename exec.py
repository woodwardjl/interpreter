#!/usr/bin/python
import _parser as parser_
import sys
import os
import evaluator
import lexer
import error_handler as eh


def main():
    file_name = __get_file_name(sys.argv)

    file_ext = __get_file_extension(file_name)

    if file_ext != ".fyp":
        eh.print_and_exit("error: invalid file extension: must be .fyp")

    if not __file_exists(file_name):
        eh.print_and_exit("error: file does not exist!")

    f = open(file_name)

    _lex    = lexer.Lexer(f.read())
    _parser = parser_.Parser(_lex.tokenize().tokens)
    _eval   = evaluator.Evaluator(_parser)

    if _eval.tokens[0] != "begin":
        eh.print_and_exit("error: first function must be 'begin'!")

    _eval.eval()

def __get_file_name(arg: list):
    return arg[1]

def __get_file_extension(arg: str):
    return os.path.splitext(arg)[1]

def __file_exists(arg: str):
    return os.path.isfile(arg)

main()