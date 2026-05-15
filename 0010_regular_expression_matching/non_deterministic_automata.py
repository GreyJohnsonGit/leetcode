from parser import Star, Start, String, Token

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