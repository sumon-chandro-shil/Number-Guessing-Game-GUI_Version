# Updated GUI Game: Now includes player name, score, and timer...

import tkinter as tk
import random
import time

# Main class: NumberGuessingGame...
class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game") # Setting in-game variables...
        self.root.geometry("450x400")

        # Adjusting the window title and size...
        self.level = tk.StringVar()
        self.level.set("Easy")

        # A variable for the level dropdown box...
        self.low = 1
        self.high = 10
        self.max_chances = 3
        self.remaining_chances = 3
        self.number = None
        self.score = 0
        self.start_time = None
        self.player_name = tk.StringVar()

        self.create_widgets()

    # Widget creation function...
    def create_widgets(self):
        tk.Label(self.root, text="Enter your name:").pack(pady=5)   # Name input field
        tk.Entry(self.root, textvariable=self.player_name).pack()

        tk.Label(self.root, text="Choose Difficulty Level:").pack(pady=5)
        tk.OptionMenu(self.root, self.level, "Easy", "Medium", "Hard", command=self.set_level).pack()

        self.info_label = tk.Label(self.root, text="", fg="blue")
        self.info_label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.entry.bind('<Return>', lambda event: self.check_guess())

        tk.Button(self.root, text="Guess", command=self.check_guess).pack(pady=10)

        # Guess button
        self.result_label = tk.Label(self.root, text="", fg="green")
        self.result_label.pack(pady=5)

        self.chances_label = tk.Label(self.root, text="", fg="purple")
        self.chances_label.pack(pady=5)

        self.score_label = tk.Label(self.root, text="Score: 0", fg="brown")
        self.score_label.pack(pady=5)

        self.timer_label = tk.Label(self.root, text="", fg="darkgreen")
        self.timer_label.pack(pady=5)

        tk.Button(self.root, text="Play Again", command=self.reset_game).pack(pady=10)

        self.set_level("Easy")  # Initialize default level...

    # Setting range and chance according to level...
    def set_level(self, value):
        if value == "Easy":
            self.low, self.high = 1, 10
            self.max_chances = 3
        elif value == "Medium":
            self.low, self.high = 1, 50
            self.max_chances = 3
        elif value == "Hard":
            self.low, self.high = 1, 100
            self.max_chances = 5
        self.reset_game()

    # To start a new round...
    def reset_game(self):
        self.number = random.randint(self.low, self.high)
        self.remaining_chances = self.max_chances
        self.entry.delete(0, tk.END)
        self.result_label.config(text="", fg="green")
        self.info_label.config(text=f"Guess the number between {self.low} and {self.high}")
        self.chances_label.config(text=f"Remaining Chances: {self.remaining_chances}")
        self.start_time = time.time()
        self.timer_label.config(text="")
        self.update_timer()

    # Timer update function...
    def update_timer(self):
        if self.remaining_chances > 0:
            elapsed = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time Elapsed: {elapsed} seconds")
            self.root.after(1000, self.update_timer)

    # Check what the user guessed...
    def check_guess(self):
        if self.remaining_chances <= 0:
            self.result_label.config(text="No more chances left. You lost!", fg="red")
            return

        try:
            guess = int(self.entry.get())
            if guess < self.low or guess > self.high:
                self.result_label.config(text=f"Enter a number between {self.low} and {self.high}", fg="red")
                return

            if guess == self.number:
                elapsed = int(time.time() - self.start_time)
                self.result_label.config(
                    text=f"Congratulations {self.player_name.get()}! You guessed it right in {elapsed} seconds!",
                    fg="green"
                )
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.remaining_chances = 0
            else:
                self.remaining_chances -= 1
                if guess < self.number:
                    self.result_label.config(text="Too low. Try again!", fg="orange")
                else:
                    self.result_label.config(text="Too high. Try again!", fg="orange")

                if self.remaining_chances == 0:
                    self.result_label.config(
                        text=f"You lost! The correct number was {self.number}.",
                        fg="red"
                    )

            self.chances_label.config(text=f"Remaining Chances: {self.remaining_chances}")

        except ValueError:
            self.result_label.config(text="Invalid input! Enter a valid number.", fg="red")

# Main code run...
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

