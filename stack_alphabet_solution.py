class  Stack_to_reverse  :
    # Create an empty stack.
    def __init__(self):
        self.alphabet = []
 
    # Return True for empty and False otherwise.
    def is_empty(self):
        return len(self.alphabet) == 0
 
    # Remove topmost element from stack.
    def pop(self):
        return self.alphabet.pop() 
 
    # Push element on top of stack.
    def push(self, letters):
        self.alphabet.append(letters)
        return letters
 
    # Function to reverse phrase
    def reverse(self, new_phrase):
        n = len(new_phrase)
 
        # Push the elements of the string to stack
        for i in range(0,n):
            your_letters.push(new_phrase[i])
 
        # Making the string empty since all characters are saved in stack
        new_phrase=""

        # Pop all letters and return to new_phrase
        for i in range(0,n):
            new_phrase+=your_letters.pop()
        return new_phrase
 
your_letters = Stack_to_reverse()

phrase = 'BabyBuggyBumpers'
reversed_phrase = your_letters.reverse(phrase)

print(f"Reversed phrase is: {reversed_phrase}")
