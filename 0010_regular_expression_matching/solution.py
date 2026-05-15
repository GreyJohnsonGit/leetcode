from parser import Parser
from non_deterministic_automata import NonDeterministicAutomata
from determinisitic_automata import DeterminisiticAutomata

class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        parser = Parser()
        tokens = parser.parse(pattern)
        automata = NonDeterministicAutomata(tokens)
        deterministic_automata = DeterminisiticAutomata(automata)
        return deterministic_automata.check_text(text)