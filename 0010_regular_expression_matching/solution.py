class Solution:
    # Need to handle greedy matching for "*"
    def isMatch(self, text: str, pattern: str) -> bool:
        print("== Text:", text, "Pattern:", pattern, "==")
        text_is_match = True
        text_index = 0
        for pattern_index in range(len(pattern)):
            match_character = pattern[pattern_index]
            if match_character == "*":
                print("\"*\" skip")
                continue
            
            is_zero_or_more = False
            if pattern_index + 1 < len(pattern) and pattern[pattern_index + 1] == "*":
                is_zero_or_more = True
            print(f"Expression: {match_character}{'*' if is_zero_or_more else ''}")

            text_exhausted = text_index >= len(text)
            if text_exhausted and is_zero_or_more:
                continue

            if text_exhausted and not is_zero_or_more:
                text_is_match = False
                break

            text_character = text[text_index]
            current_character_is_match = text_character == match_character or match_character == "."

            if not is_zero_or_more and not current_character_is_match:
                text_is_match = False
                break

            if not is_zero_or_more and current_character_is_match:
                text_index += 1
                continue

            while (
                text_index < len(text) 
                and (
                    text_character == match_character 
                    or match_character == "."
                )
            ):
                text_index += 1
                text_character = text[text_index] if text_index < len(text) else None
        return text_is_match and text_index >= len(text)