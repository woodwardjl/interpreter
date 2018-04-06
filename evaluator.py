import _parser
import world
import lexer
import type_helper
import error_handler as eh


class Evaluator(object):
    def __init__(self, parser: _parser.Parser):
        self.tokens = parser.tokens
        self.world = world.World()

    def eval(self) -> int or bool:
        for token in self.tokens:
            self.__eval(token)

    def __eval(self, token: list or str or int):
        if isinstance(token, list):
            if len(token) == 0:
                return
            elif len(token) == 1:
                return self.__eval(token[0])
            elif token[0] == "define":
                self.world.insert(token[1], self.__eval(token[2]))
            elif type_helper.is_math(token[0]):
                return self.__eval_math(token)
            elif token[0] == "if":
                return self.__eval_if(token)
            elif token[0] == "put":
                print(self.__eval(token[1]))
            elif token[0] == "loop":
                return self.__eval_loop(token)
            elif token[0] == "len":
                loop_count = self.__eval(token[1])

                if isinstance(loop_count, int):
                    eh.ErrorHandler.print_and_exit("invalid len of integer!")
                else:
                    return len(loop_count.replace("'", ""))
        else:
            return self.__eval_literal(token)

    def __eval_literal(self, token: int or str) -> int or str:
        if type_helper.is_keyword(token):
            return token
        else:
            if type(token) == int:
                return token
            elif type_helper.is_string(token):
                return token[1:-1]
            else:
                if token in self.world.map:
                    return self.world.map[token]
                else:
                    eh.ErrorHandler.print_and_exit(
                            "variable undefined: " + token)

    def __eval_if(self, token: list):
        if self.__eval(token[1]):
            return self.__eval(token[2])
        else:
            return self.__eval(token[3])

    def __eval_loop(self, token: list):
        if len(token) <= 2:
            return

        for i in range(self.__eval(token[1])):
            self.__eval(token[2])

    def __eval_math(self, token: list):
        if type_helper.is_basic_math(token[0]) or \
                type_helper.is_operator(token[0]):
            arg_one = self.__eval(token[1])
            arg_two = self.__eval(token[2])

            if not type(arg_one) == type(arg_two):
                eh.ErrorHandler.print_and_exit(
                        "invalid math expression: {0} {1} {2} -> "
                        "({3} {4} {5})".format(
                                token[0], type(arg_one).__name__,
                                type(arg_two).__name__, token[0],
                                arg_one, arg_two))
                return self.world.get_value(token[0])(self.__eval(token[1]),
                                                      self.__eval(token[2]))
            else:
                return self.world.get_value(token[0])(arg_one, arg_two)
        else:
            return self.world.get_value(token[0])(self.__eval(token[1]))


if __name__ == "__main__":
    lex = lexer.Lexer("(begin "
                      "(define test "
                      "(if (and (lt 50 10) (gt 10 5)) "
                      "100 "
                      "200))"
                      "(loop (len \"12345\") (put \"jamielol\")))")

    e = Evaluator(_parser.Parser(lex.tokenize().tokens))
    e.eval()
    print(e.tokens)
    print(e.world.get_value("test"))
