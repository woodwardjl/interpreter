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
        try:
            self.element_count += 1
            parsed_tokens = []

            while tokens[0] != terminator:
                parsed_tokens.append(self.parse(tokens))

            tokens.pop(0)

            return parsed_tokens
        except:
            print("unable to find terminator: \""
                  + terminator + "\"")

    def __value(self, lexeme: str) -> int or str:
        return int(lexeme) if lexeme.isdigit() else lexeme


if __name__ == "__main__":
    lexer = lexer.Lexer("(begin (define test"
                        "(if (lt 10 100)"
                        "(if (gt (mult 5 5) 24) (50) (100))"
                        "(150))) (define r 100))")
    print(Parser(lexer.tokenize().tokens).tokens)
