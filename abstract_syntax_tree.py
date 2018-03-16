import _parser as p
import lexer as l


class AST(object):
    def __init__(self, parser: p.Parser):
        self.parser = parser

    def print_ast(self, tokens: list, tab_count=0, return_list=None) -> str:
        if return_list == None:
            return_list = []

        self.__append_start(tab_count, return_list)

        for element in tokens:
            if isinstance(element, str) or isinstance(element, int):
                return_list.append("{} ".format(element))
            else:
                self.print_ast(element, tab_count + 1, return_list)

        return ''.join(return_list)

    def __str__(cls):
        return cls.print_ast(cls.parser.tokens)

    def __append_start(self, tab_count: int, return_list: list) -> None:
        return_list.append("\n")
        [return_list.append("  ") for i in range(tab_count)]


if __name__ == "__main__":
    lexer = l.Lexer("("
                        "(define test"
                        "(if (lt 10 100)"
                        "(if (gt (mult 5 5) 24) (50) (100))"
                        "(150))) "
                        "(define r 100) "
                        "(define x (mult 10 10))"
                        ")")
    print(AST(p.Parser(lexer.tokenize().tokens)))
