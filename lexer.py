import utility as u


class Lexer(object):
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.string_seperator = "g9zqbJSMLDdvkxO"
        self.right_brace_seperator = "dODIQWPODIdqipdwqi"
        self.left_brace_seperator = "dqwk980182DOIQWDJOIDJW"
        self.tokens = []

    def tokenize(self) -> "Lexer":
        self.__arrange_strings(" ", self.string_seperator)
        self.__arrange_strings("(", self.left_brace_seperator)
        self.__arrange_strings(")", self.right_brace_seperator)

        self.tokens = self.source_code \
            .replace("(", " ( ") \
            .replace(")", " ) ") \
            .split()

        self.__test(self.string_seperator, " ")
        self.__test(self.left_brace_seperator, "(")
        self.__test(self.right_brace_seperator, ")")

        return self

    def __arrange_strings(self, to_find, to_replace):
        i = 0
        while i < len(self.source_code):
            if u.is_char(self.source_code[i], "\""):
                i += 1
                if i >= len(self.source_code):
                    return

                while not u.is_char(self.source_code[i], "\""):
                    if u.is_char(self.source_code[i], to_find):
                        self.source_code = ''.join(self.source_code[:i]) \
                                           + to_replace \
                                           + ''.join(self.source_code[i + 1:])
                    i += 1
            i += 1

    def __test(self, seperator, replacement):
        for index, item in enumerate(self.tokens):
            self.tokens[index] = u.replace_in_str(item,
                                                  seperator,
                                                  replacement)

    def __str__(cls):
        return str(cls.tokens)


if __name__ == "__main__":
    lex = Lexer("(begin (var testvar \" 123 (123) 123\"))")
    lex.tokenize()
