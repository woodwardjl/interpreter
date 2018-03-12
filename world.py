import operator as o
import mymath as m
import error_handler as eh

class World(object):
    def __init__(self):
        self.map = {"mult": o.mul,
                    "plus": o.add,
                    "div": o.floordiv,
                    "minus": o.sub,
                    "lt": o.lt,
                    "gt": o.gt,
                    "lteq": m.lteq,
                    "gteq": m.gteq,
                    "iseq": o.eq,
                    "noteq": m.noteq}

    def insert(self, key: int or str, value: int or str):
        self.map[key] = value

    def get(self, key) -> int or str:
        try:
            return self.map[key]
        except:
            eh.ErrorHandler.print_and_exit("key (" + key + "): key does not exist!")

if __name__ == "__main__":
    w = World()
    print(w.get("mult")(10, 5))


