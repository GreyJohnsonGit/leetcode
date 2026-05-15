from parser import Parser
from non_deterministic_automata import NonDeterministicAutomata
from determinisitic_automata import DeterminisiticAutomata

class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        print("== Text:", text, "Pattern:", pattern, "==")
        parser = Parser()
        tokens = parser.parse(pattern)
        automata = NonDeterministicAutomata(tokens)
        deterministic_automata = DeterminisiticAutomata(automata)
        print("Tokens:", [str(token) for token in tokens])
        print("ND Automata:", automata)
        print("D Automata:", deterministic_automata)
        return deterministic_automata.check_text(text)