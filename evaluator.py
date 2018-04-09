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
        self.remove_vars = []

        self.__eval_map = {
            "if":    self.__eval_if,
            "put":   self.__eval_put,
            "putln": self.__eval_putln,
            "loop":  self.__eval_loop,
            "len":   self.__eval_len}

    def eval(self) -> int or bool:
        for token in self.tokens:
            self.__eval(token)

    def __eval(self, token: list or str or int):
        if isinstance(token, list):
            self.remove_vars = self.__get_remove_vars(token)
            if len(token) == 0:
                return
            elif len(token) == 1:
                if type(token[0]) != list:
                    if self.world.func_map_has_key(token[0]):
                        return self.__eval_func(token[0], [])
                return self.__eval(token[0])
            elif token[0] == "var":
                self.world.insert(token[1], self.__eval(token[2]))
            elif token[0] == "func":
                if len(token) > 3:
                    if len(token[3]) > 1:
                        token[3] = [tok for tok in token[3:]]
                    else:
                        token[3] = token[3][0]
                self.world.insert_func(token[1], token[2], token[3])
            elif type_helper.is_math(token[0]) or type_helper.is_operator(
                    token[0]):
                return self.__eval_math(token)
            elif type(token[0]) != list and token[0] not in self.__eval_map:
                if self.world.func_map_has_key(token[0]):
                    return self.__eval_func(token[0], token[1:])
                else:
                    return self.world.get_value(token[0])(
                            self.__eval(token[1]))
            else:
                if type(token[0]) != list:
                    return self.__eval_map[token[0]](token)
                else:
                    for item in token:
                        self.__eval(item)
        else:
            return self.__eval_literal(token)

    def __eval_literal(self,
                       token: int or str or float) -> int or str or float:
        if type_helper.is_keyword(token):
            return token
        else:
            if type(token) == int or type(token) == float:
                return token
            elif type_helper.is_string(token):
                return token[1:-1]
            else:
                if self.world.map_has_key(token):
                    return self.world.get_value(token)
                elif self.world.func_map_has_key(token):
                    return self.__eval_func(token, [])
                else:
                    eh.print_and_exit("variable undefined: " + token)

    def __eval_if(self, token: list):
        if self.__eval(token[1]):
            return self.__eval(token[2])
        else:
            return self.__eval(token[3])

    def __eval_loop(self, token: list):
        if len(token) <= 2:
            return

        loop_count = self.__eval(token[1])

        if type(loop_count) == str:
            eh.print_and_exit("invalid loop count: " + loop_count)

        for i in range(int(loop_count)):
            self.__eval(token[2])

    def __eval_math(self, token: list):
        arg_one = self.__eval(token[1])
        arg_two = self.__eval(token[2])

        if utility.is_two_different_types(str, arg_one, arg_two):
            eh.print_and_exit("invalid math expression: {0} {1} {2} -> "
                              "({3} {4} {5})"
                              .format(token[0], type(arg_one).__name__,
                                      type(arg_two).__name__, token[0],
                                      arg_one, arg_two))
            return self.world.get_value(token[0])(self.__eval(token[1]),
                                                  self.__eval(token[2]))

        if utility.is_different_numeric_type(arg_one, arg_two):
            arg_one = float(arg_one)
            arg_two = float(arg_two)

        return self.world.get_value(token[0])(arg_one, arg_two)

    def __eval_put(self, token: list or str or int, endl=""):
        result = self.__eval(token[1])

        if result == None:
            print()
        elif type(result) == str:
            [print(section) for section in result.split("\\n")]
        else:
            print(result)

    def __eval_putln(self, token: list or str or int):
        self.__eval_put(token, "\n")

    def __eval_len(self, token: list or str or int):
        loop_count = self.__eval(token[1])
        if type(loop_count) == int:
            eh.print_and_exit("invalid len of integer!")
        else:
            return len(loop_count.replace("'", ""))

    def __eval_func(self, func_name: str, args: list):
        func_copy = self.world.get_func_copy(func_name)

        if len(args) != len(func_copy["args"]):
            eh.print_and_exit("func ("
                              + func_name
                              + "): invalid argument count!")

        for index, item in enumerate(func_copy["args"]):
            utility.replace_in_list(func_copy["source"], item, args[index])

        return_eval = self.__eval(func_copy["source"])
        self.world.remove_vars(self.__get_remove_vars(func_copy["source"]))

        return return_eval

    def __get_remove_vars(self, token: list):
        to_return = []

        for index, item in enumerate(token):
            if type(item) == list:
                if utility.is_list_of_lists(item):
                    to_return += self.__get_remove_vars(item)
                else:
                    if len(item) < 2:
                        continue

                    if item[0] == "var":
                        to_return.append(item[1])

        return to_return


if __name__ == "__main__":
    lex = lexer.Lexer("""
    (begin

  (func test (x y) (
    (y)
  ))
    
    (putln "Testing local var....")
    (test 10 (put 200))
    
    )

    """)

    e = Evaluator(_parser.Parser(lex.tokenize().tokens))
    print(e.tokens)
    e.eval()
