import operator as o
import mymath as m

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
        return self.map[key]


if __name__ == "__main__":
    w = World()
    print(w.get("mult")(10, 5))


