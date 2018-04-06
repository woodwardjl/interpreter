import _parser
import world
import lexer
import type_helper
import error_handler as eh
import utility


class Evaluator(object):
    def __init__(self, parser: _parser.Parser):
        self.tokens = parser.tokens
        self.world = world.World()
        self.__eval_map = {
            "if":   self.__eval_if,
            "put":  self.__eval_put,
            "loop": self.__eval_loop,
            "len":  self.__eval_len}

    def eval(self) -> int or bool:
        for token in self.tokens:
            self.__eval(token)

    def __eval(self, token: list or str or int):
        if isinstance(token, list):
            if len(token) == 0:
                return
            elif len(token) == 1:
                return self.__eval(token[0])
            elif token[0] == "var":
                self.world.insert(token[1], self.__eval(token[2]))
            elif token[0] == "func":
                self.world.insert_func(token[1], token[2], token[3])
            elif type_helper.is_math(token[0]) or type_helper.is_operator(
                    token[0]):
                return self.__eval_math(token)
            elif token[0] not in self.__eval_map:
                if self.world.func_map_has_key(token[0]):
                    return self.__eval_func(token[0], token[1:])
                else:
                    return self.world.get_value(token[0])(
                            self.__eval(token[1]))
            else:
                tok = token[0]
                return self.__eval_map[tok](token)

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
                if self.world.map_has_key(token):
                    return self.world.get_value(token)
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

    def __eval_put(self, token: list or str or int):
        print(self.__eval(token[1]))

    def __eval_len(self, token: list or str or int):
        loop_count = self.__eval(token[1])
        if isinstance(loop_count, int):
            eh.ErrorHandler.print_and_exit("invalid len of integer!")
        else:
            return len(loop_count.replace("'", ""))

    def __eval_func(self, func_name: str, args: list):
        func = self.world.get_func(func_name)

        if len(args) != len(func["args"]):
            eh.ErrorHandler.print_and_exit(
                    "func (" + func_name + "): invalid argument count!")

        # need to swap values
        for item in args:
            for func_arg in func["args"]:
                utility.replace_in_list(func["source"], func_arg, item)

        return self.__eval(func["source"])


if __name__ == "__main__":
    lex = lexer.Lexer("""
    
                      (begin
                        (func cube (x) 
                          (^ x 3))
                        (func sqr (x) 
                          (* x x))
                        (func my_pow (x y)
                          (^ x y))
                          
                        (put 
                          (if (< (cube 10) 1000) 
                            (sqr 10) 
                            (sqr 9)))
                          
                        (var cubetest (cube 10))
                        (var powtest (my_pow 3 3))
                      
                        (put cubetest)
                        (put powtest)
                      )                  
                      
                      """)

    # lex = lexer.Lexer("(begin "
    #                   "(var test "
    #                   "(if (and (lt 50 10) (gt 10 5)) "
    #                   "100 "
    #                   "200))"
    #                   "(loop (len \"12345\") (var test (plus test 10)))"
    #                   ")")

    e = Evaluator(_parser.Parser(lex.tokenize().tokens))
    e.eval()
    print(e.tokens)
