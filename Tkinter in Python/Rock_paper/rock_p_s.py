import tkinter as tk
from PIL import Image, ImageTk
import random

# Function to determine the result
def play():
    choices = ["Rock", "Paper", "Scissors"]
    user_choice = random.choice(choices)
    computer_choice = random.choice(choices)

    # Update images
    user_image_label.config(image=images[user_choice])
    computer_image_label.config(image=images[computer_choice])

    # Determine the result
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    # Display the result
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Load images for Rock, Paper, Scissors
images = {
    "Rock": ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100))),
    "Paper": ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100))),
    "Scissors": ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100))),
}

# Labels for showing user and computer choices
user_label = tk.Label(root, text="You:")
user_label.pack()

user_image_label = tk.Label(root)
user_image_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer:")
computer_label.pack()

computer_image_label = tk.Label(root)
computer_image_label.pack(pady=10)

# Button to play the game
play_button = tk.Button(root, text="Play", command=play)
play_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the application
root.mainloop()
