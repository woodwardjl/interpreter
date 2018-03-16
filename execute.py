import _parser as parser_
import sys
import evaluator
import lexer
import error_handler as eh


def main():
    f = open(sys.argv[1])
    _lex = lexer.Lexer(f.read())
    _parser = parser_.Parser(_lex.tokenize().tokens)
    _eval = evaluator.Evaluator(_parser)
    if _eval.tokens[0] != "begin":
        eh.ErrorHandler.print_and_exit("first function must be 'begin'!")
    print(_eval.tokens)

main()