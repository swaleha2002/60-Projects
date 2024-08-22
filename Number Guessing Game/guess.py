# Number Guessing Game:
# Create a game where the computer generates a random number, and the player has to guess it.
# Add features like providing hints (too high/too low) and limiting the number of attempts.

import tkinter as tk
from tkinter import messagebox
import random

# Initialize the game
class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.n = random.randint(1, 100)  # Generate a random number
        self.guess_count = 0  # Counter for attempts

        # Create GUI elements
        self.label = tk.Label(root, text="Guess a number between 1 and 100")
        self.label.pack(pady=20)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=20)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=20)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.guess_count += 1

            if user_guess < self.n:
                messagebox.showinfo("Result", "Higher number, please!")
            elif user_guess > self.n:
                messagebox.showinfo("Result", "Lower number, please!")
            else:
                messagebox.showinfo("Congratulations!",
                                    f"You guessed the number {self.n} correctly in {self.guess_count} attempts!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")

    def reset_game(self):
        self.n = random.randint(1, 100)
        self.guess_count = 0
        self.entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()

# Instantiate the game
game = NumberGuessingGame(root)

# Run the main loop
root.mainloop()

        
       
