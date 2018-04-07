import lexer
import error_handler as eh


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
            eh.print_and_exit("unable to find function terminator: \""
                              + terminator + "\"")

    def __value(self, lexeme: str) -> int or str:
        try:
            return int(lexeme)
        except:
            try:
                return float(lexeme)
            except:
                return lexeme
