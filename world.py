import operator as o
import mymath as m
import error_handler as eh
import math


class World(object):
    def __init__(self):
        self.__map = {  # Basic Math
            "*":      o.mul,
            "+":      o.add,
            "/":       o.floordiv,
            "-":     o.sub,
            "^":       o.pow,
            "%":       o.mod,
            "max":       m.max,
            "min":       m.min,
            # Advanced Math
            "abs":       o.abs,
            "factorial": math.factorial,
            "sqrt":      math.sqrt,
            "neg":       o.neg,
            # Operators
            "<":         o.lt,
            ">":         o.gt,
            "<=":        m.lteq,
            ">=":        m.gteq,
            "==":        o.eq,
            "!=":        m.noteq,
            "&&":        o.and_}

        self.func_map = {}

    def insert(self, key: int or str, value: int or str):
        self.__map[key] = value

    def insert_func(self, name: str, args: list, source: list):
        self.func_map[name] = {"args": args, "source": source, "vars": None}

    def get_func(self, key: str):
        try:
            return self.func_map[key]
        except:
            eh.ErrorHandler.print_and_exit(
                    "func (" + key + "): func does not exist!")

    def get_value(self, key) -> int or str:
        try:
            return self.__map[key]
        except:
            eh.ErrorHandler.print_and_exit(
                    "key (" + key + "): key does not exist!")

    def get_key(self, value):
        for k, v in self.__map.items():
            if v == value:
                return k
        return None

    def map_has_key(self, key: int or str):
        return key in self.__map

    def func_map_has_key(self, key: int or str):
        return key in self.func_map


if __name__ == "__main__":
    w = World()
    print(w.get_value("mult")(10, 5))
