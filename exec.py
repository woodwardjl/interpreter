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

    _file = open(file_name)
    _lex = lexer.Lexer(' '.join(
            [line.rstrip("\n") for line in _file if not __is_comment(line)]))
    _tokens = _lex.tokenize().tokens

    is_test = False

    if len(_tokens) > 1 and _tokens[2] == "test":
        is_test = True
        _tokens = _tokens[0:2] + _tokens[3:]

    _parser = parser_.Parser(_tokens)
    _eval = evaluator.Evaluator(_parser, is_test)

    if _eval.tokens[0] != "begin":
        eh.print_and_exit("error: first function must be 'begin'!")

    _eval.eval()
    print()


def __get_file_name(arg: list):
    return arg[1]


def __get_file_extension(arg: str):
    return os.path.splitext(arg)[1]


def __file_exists(arg: str):
    return os.path.isfile(arg)


def __is_comment(arg: str):
    return str.startswith(arg.strip(' '), "--")


main()
