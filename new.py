import os

def main():
    problem_number = None
    is_valid_response = False
    while not is_valid_response:
        print("Enter problem number (ex. 1, 5, 10, etc.):")
        problem_number = input()
        if not problem_number.isdigit():
            print("Invalid problem number. Please enter a valid number.")
        else:
            is_valid_response = True
            problem_number = int(problem_number)
    
    problem_name = None
    is_valid_response = False
    while not is_valid_response:
        print("Enter problem name (ex. Two Sum, Longest Substring, etc.):")
        problem_name = input()
        not_valid_characters = not all(c.isalnum() or c.isspace() for c in problem_name)
        too_short = not len(problem_name.strip()) > 0
        if not_valid_characters:
            print("Invalid problem name. Please enter a valid name ([a-zA-Z0-9 ]).")
        elif too_short:
            print("Invalid problem name. Please enter a valid name (at least one character).")
        else:
            is_valid_response = True
            problem_name = problem_name.strip().lower().replace(" ", "_")

    folder_name = f"{str(problem_number).zfill(4)}_{problem_name}"

    is_valid_response = False
    while not is_valid_response:
        print(f"Folder Name: {folder_name}")
        print("Is this Correct? (y/n)")
        response = input().lower()
        if response == "y":
            is_valid_response = True
        elif response == "n":
            return -1
        else:
            print("Invalid response. Please enter 'y' or 'n'.")
    
    if os.path.exists(folder_name):
        print(f"Folder '{folder_name}' already exists. Please choose a different problem number or name.")
        return -1
    
    os.makedirs(folder_name)
    with open(os.path.join(folder_name, "solution.py"), "w") as file:
        file.write("""
class Solution(object):
    def solve(self, *args):
                   """.strip())

    with open(os.path.join(folder_name, "test.py"), "w") as file:
        file.write("""
import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

if __name__ == "__main__":
    unittest.main(verbosity=0)
                """.strip())
        
    return 0

if __name__ == "__main__":
    main()