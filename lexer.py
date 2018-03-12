class Lexer(object):
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.tokens = []

    def tokenize(self) -> "Lexer":
        self.tokens = self.source_code \
            .replace("(", " ( ") \
            .replace(")", " ) ") \
            .split()

        return self

    def __str__(cls):
        return str(cls.tokens)


if __name__ == "__main__":
    l = Lexer("(mult (plus 10 5) (neg 10 5))")
    print(l.tokenize())
