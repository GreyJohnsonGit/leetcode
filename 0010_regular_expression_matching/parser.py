class String:
    def __init__(self, pattern, start_index: int, end_index: int) -> String:
        self.definition = pattern[start_index:end_index]
        self.length = len(self.definition)
      
    def __str__(self) -> str:
        return F"<String: {self.definition}>"

class Star:
    def __init__(self, pattern, start_index: int, end_index: int) -> Star:
        self.definition = pattern[start_index:end_index].replace("*", "")
        if "." in self.definition:
            self.definition = '.'
        self.length = len(self.definition)

    def __str__(self) -> str:
        return F"<Star: {self.definition}>"
    
class Start:
    def __str__(self) -> str:
        return "<Start>"

type Token = String | Star | Start

class Parser:
    def parse(self, pattern: str) -> Parser:
        pattern = pattern
        tokens = [Start()]
        pattern_index = 0
        mode = "string"
        if len(pattern) > 1 and pattern[1] == "*":
            mode = "star"

        while pattern_index < len(pattern):
            if mode == "string":
                next_star_index = pattern.find("*", pattern_index)
                if next_star_index == -1:
                    tokens.append(String(pattern, pattern_index, len(pattern)))
                    break
                tokens.append(String(pattern, pattern_index, next_star_index - 1))
                pattern_index = next_star_index - 1
                mode = "star"
                continue
            
            if mode == "star":
                last_star_index = pattern_index + 1
                while last_star_index + 2 < len(pattern) and pattern[last_star_index + 2] == "*":
                    last_star_index += 2
                tokens.append(Star(pattern, pattern_index, last_star_index))
                pattern_index = last_star_index + 1
                mode = "string"
        return tokens