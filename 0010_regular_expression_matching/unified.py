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
            print("Character:", pattern[pattern_index], "Mode:", mode, "Index:", pattern_index)
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
  
class NonDeterministicAutomata:
    def __init__(self, tokens: list[Token]) -> NonDeterministicAutomata:
        self.exit_states = []
        if isinstance(tokens[-1], Star):
            for index in range(tokens[-1].length):
                self.exit_states.append((len(tokens) - 1, index))
            if isinstance(tokens[-2], String):
                self.exit_states.append((len(tokens) - 2, tokens[-2].length - 1))
        else:
            self.exit_states.append((len(tokens) - 1, tokens[-1].length - 1))

        self.transitions = {}
        self.from_lookup = {}
        for token_index in range(len(tokens)):
            token = tokens[token_index]
            next_token_exists = token_index + 1 < len(tokens)
            next_string_token_exists = next_token_exists and token_index + 2 < len(tokens)

            if isinstance(token, Start):
                if next_token_exists:
                    next_token = tokens[token_index + 1]
                    if isinstance(next_token, String):
                        to_character = next_token.definition[0]
                        self.add_transition(
                            (token_index, 0), 
                            (to_character, token_index + 1, 0)
                        )

                    if isinstance(next_token, Star):
                        for index in range(next_token.length):
                            to_character = next_token.definition[index]
                            self.add_transition(
                                (token_index, 0), 
                                (to_character, token_index + 1, index)
                            )

                        if next_string_token_exists:
                            to_character = tokens[token_index + 2].definition[0]
                            self.add_transition(
                                (token_index, 0), 
                                (to_character, token_index + 2, 0)
                            )

                    

            if isinstance(token, String):
                # Adjacent Transitions
                for index in range(token.length - 1):
                    from_character = token.definition[index]
                    to_character = token.definition[index + 1]
                    self.from_lookup[(token_index, index)] = from_character
                    self.add_transition(
                        (token_index, index), 
                        (to_character, token_index, index + 1)
                    )

                # Skip * Transitions
                if next_token_exists:
                    next_token = tokens[token_index + 1]
                    for next_token_index in range(next_token.length):
                        from_character = token.definition[token.length - 1]
                        to_character = next_token.definition[next_token_index]
                        self.from_lookup[(token_index, token.length - 1)] = from_character
                        self.add_transition(
                            (token_index, token.length - 1), 
                            (to_character, token_index + 1, next_token_index)
                        )

                # Skip All of the * Transitions
                if next_string_token_exists:
                    from_character = token.definition[token.length - 1]
                    to_character = tokens[token_index + 2].definition[0]
                    self.from_lookup[(token_index, token.length - 1)] = from_character
                    self.add_transition(
                        (token_index, token.length - 1), 
                        (to_character, token_index + 2, 0)
                    )

            if isinstance(token, Star):
                # Cycle Transitions
                for index in range(token.length):
                    character = token.definition[index]
                    self.from_lookup[(token_index, index)] = character
                    self.add_transition(
                        (token_index, index), 
                        (character, token_index, index)
                    )

                # Jump Transitions
                for index in range(token.length):
                    for jump_location_index in range(index + 1, token.length):
                        from_character = token.definition[index]
                        to_character = token.definition[jump_location_index]
                        self.from_lookup[(token_index, index)] = from_character
                        self.add_transition(
                          (token_index, index), 
                          (to_character, token_index, jump_location_index)
                        )
                    if next_token_exists:
                        from_character = token.definition[index]
                        to_character = tokens[token_index + 1].definition[0]
                        self.from_lookup[(token_index, index)] = from_character
                        self.add_transition(
                            (token_index, index), 
                            (to_character, token_index + 1, 0)
                        )

    def __str__(self) -> str:
        accumulator = "<Non-Deterministic Automata: \n"
        for from_key, to_keys in self.transitions.items():
            accumulator += f"  {from_key} -> {to_keys}\n"
        accumulator += ">"
        return accumulator

    def add_transition(self, from_key: tuple[int, int], to_key: tuple[str, int, int]) -> None:
        self.transitions.setdefault(from_key, []).append(to_key)

class DeterminisiticAutomata:
    def __init__(self, non_deterministic_automata: NonDeterministicAutomata) -> DeterminisiticAutomata:
        self.transitions: dict[frozenset[tuple[int, int]], dict[str, frozenset[tuple[int, int]]]] = {}
        self.exit_states = non_deterministic_automata.exit_states

        get_nd_transitions = self.build_get_nd_transitions(non_deterministic_automata)
        
        states_to_visit = [frozenset({(0, 0)})]
        while len(states_to_visit) > 0:
            state = states_to_visit.pop()
            nd_transitions = get_nd_transitions(state)
            dot_transitions = [e for e in nd_transitions if e[0] == "."]

            for character, token_index, index in nd_transitions:
                to_state = (token_index, index)
                state_transitions: dict[str, frozenset[tuple[int, int]]] = self.transitions.setdefault(state, {})
                character_transition = state_transitions.setdefault(character, frozenset())
                character_transition = character_transition.union({to_state})
                for _, token_index, index in dot_transitions:
                    dot_to_state = (token_index, index) 
                    character_transition = character_transition.union({dot_to_state})
                state_transitions[character] = character_transition
                if character_transition not in self.transitions:
                    states_to_visit.append(character_transition)
        
    def __str__(self) -> str:
        accumulator = "<Deterministic Automata:\n"
        for from_key, to_keys in self.transitions.items():
            from_key_stringified = "{" + ", ".join([f"({state_index}, {token_index})" for state_index, token_index in from_key]) + "}"
            to_keys_stringified = str(to_keys).replace("frozenset({", "{").replace("})", "}")
            accumulator += f"  {from_key_stringified} -> {to_keys_stringified}\n"
        accumulator += ">"
        return accumulator

    def build_get_nd_transitions(self, non_deterministic_automata: NonDeterministicAutomata):
        def get_nd_transitions(state: frozenset[tuple[int, int]]) -> list[tuple[str, tuple[int, int]]]:
            transitions = []
            for sub_state in state:
                transitions.extend(non_deterministic_automata.transitions.get(sub_state, []))
            return transitions
        
        return get_nd_transitions
    
    def check_text(self, text: str) -> bool:
        current_state = frozenset({(0, 0)})
        for character in text:
            state_transitions = self.transitions.get(current_state, None)
            if state_transitions is None:
                return False
            transition_state = state_transitions.get(character, None)
            if transition_state is None:
                transition_state = state_transitions.get(".", None)
            if transition_state is None:
                return False
            
            current_state = transition_state
        return any(exit_state in current_state for exit_state in self.exit_states)
    
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        parser = Parser()
        tokens = parser.parse(pattern)
        automata = NonDeterministicAutomata(tokens)
        deterministic_automata = DeterminisiticAutomata(automata)
        return deterministic_automata.check_text(text)