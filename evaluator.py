import parser
import world
import lexer
import type_helper as th


class Evaluator(object):
    def __init__(self, parser: parser.Parser):
        self.tokens = parser.tokens
        self.world = world.World()

    def eval(self) -> int or bool:
        for token in self.tokens:
            self.__eval(token)

    def __eval(self, token: list or str or int):
        if isinstance(token, list):
            if len(token) == 1:
                return self.__eval(token[0])
            elif token[0] == "define":
                self.world.insert(self.__eval(token[1]), self.__eval(token[2]))
            elif th.is_operator(token[0]) or th.is_comparison(token[0]):
                return self.world.get(token[0])(self.__eval(token[1]),
                                                self.__eval(token[2]))
            elif token[0] == "if":
                if self.__eval(token[1]):
                    return self.__eval(token[2])
                else:
                    return self.__eval(token[3])
        else:
            return token


if __name__ == "__main__":
    lexer = lexer.Lexer("("
                        "(define test"
                        "(if (lt 10 100)"
                        "(if (gt (mult 5 5) 24) (50) (100))"
                        "(150))) "
                        "(define r 100) "
                        "(define x (mult 10 10))"
                        ")")
    e = Evaluator(parser.Parser(lexer.tokenize().tokens))
    e.eval()
    print(e.world.get("y"))

