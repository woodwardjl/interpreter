import parser as p
import lexer as l


class AST(object):
    def __init__(self, parser: p.Parser):
        self.parser = parser

    def print_ast(self, tokens: list, tab_width=0, return_str=[]) -> str:
        return_str.append("\n")
        [return_str.append("  ") for i in range(tab_width)]

        for element in tokens:
            if isinstance(element, str) or isinstance(element, int):
                return_str.append("{} ".format(element))
            else:
                self.print_ast(element, tab_width + 1, return_str)

        return ''.join(return_str)

    def __str__(self):
        return self.print_ast(self.parser.tokens)


if __name__ == "__main__":
    lexer = l.Lexer("(begin (define r 10) (add (mult r r) (div 10 2)))")
    print(AST(p.Parser(lexer.tokenize().tokens)))
