from parser import Token
from non_deterministic_automata import NonDeterministicAutomata

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