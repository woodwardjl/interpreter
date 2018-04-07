import utility as u


class Lexer(object):
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.string_seperator = "g9zqbJSMLDdvkxO"
        self.tokens = []

    def tokenize(self) -> "Lexer":
        self.__arrange_strings()

        self.tokens = self.source_code \
            .replace("(", " ( ") \
            .replace(")", " ) ") \
            .split()

        for index, item in enumerate(self.tokens):
            self.tokens[index] = u.replace_in_str(item,
                                                  self.string_seperator,
                                                  " ")

        return self

    def __arrange_strings(self):
        i = 0
        while i < len(self.source_code):
            if u.is_char(self.source_code[i], "\""):
                i += 1
                while not u.is_char(self.source_code[i], "\""):
                    i += 1
                    if i >= len(self.source_code):
                        return
                    if self.source_code[i].isspace():
                        self.source_code = self.source_code[:i] \
                                           + self.string_seperator \
                                           + self.source_code[i + 1:]
            i += 1

    def __str__(cls):
        return str(cls.tokens)
