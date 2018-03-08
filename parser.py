import lexer


class Parser(object):
    def __init__(self, tokens: list):
        self.element_count = 0
        self.tokens = self.parse(tokens)

    def parse(self, tokens: list) -> int or list:
        token = tokens.pop(0)

        if token == "(":
            return self.__parse_until(tokens, ")")
        else:
            return self.__value(token)

    def __parse_until(self, tokens: list, terminator: str) -> list:
        self.element_count += 1
        f = []
        while tokens[0] != terminator:
            f.append(self.parse(tokens))
        tokens.pop(0)

        return f

    def __value(self, lexeme: str) -> int or str:
        return int(lexeme) if lexeme.isdigit() else lexeme

if __name__ == "__main__":
    lexer = lexer.Lexer("(begin (define r 10) (add (mult r r) (div 10 2)))")
    print(Parser(lexer.tokenize().tokens).tokens)
