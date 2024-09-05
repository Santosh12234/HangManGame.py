from tkinter import *
import random

root = Tk()
root.geometry("700x700")
root.title("HANG MAN GAME")
root.resizable(False, True)

canvas = Canvas(root, width=500, height=260)
canvas.pack(pady=30)
canvas.create_line(150, 260, 250, 260, width=3)
canvas.create_line(200, 260, 200, 40, width=3)
canvas.create_line(200, 90, 250, 40, width=3)
canvas.create_line(200, 40, 300, 40, width=3)
canvas.create_line(300, 40, 300, 70, width=3)

label1 = Label(root, font=("Candara", 25, "bold"))
label1.pack()

guess_entry = Entry(root, font=("Candara", 25, "bold"), justify=CENTER, relief=GROOVE, bd=5, bg="#D3D3D3")
guess_entry.pack(pady=10)

button1 = Button(root, text="Guess", font=('Candara', 25, "bold"), relief=GROOVE, bd=2, fg="white", bg="green", width=8, command=lambda: check_guess())
button1.place(x=200, y=550)

button2 = Button(root, text="Exit", font=('Candara', 25, "bold"), relief=GROOVE, bd=2, fg="white", bg="red", width=8, command=root.quit)
button2.place(x=360, y=550)

result_label = Label(root, font=("Candara", 25, "bold"))
result_label.place(x=150, y=475)

words = ['santosh', 'siddhu', 'lokesh', 'npandu', 'harsha', 'narayana', 'sriram', 'prudhvi']
mistakes = 0
word = ""
word_with_blanks = ""

def choose_word():
    return random.choice(words)

def update_hangman(mistakes):
    if mistakes == 1:
        canvas.create_oval(280, 70, 320, 100, width=3)
    elif mistakes == 2:
        canvas.create_line(300, 100, 300, 180, width=3)
    elif mistakes == 3:
        canvas.create_line(300, 105, 270, 155, width=3)
    elif mistakes == 4:
        canvas.create_line(300, 105, 330, 155, width=3)
    elif mistakes == 5:
        canvas.create_line(300, 180, 270, 230, width=3)
    elif mistakes == 6:
        canvas.create_line(300, 180, 330, 230, width=3)

def check_guess():
    global word_with_blanks, mistakes
    guess = guess_entry.get().strip().lower()
    if guess in word:
        new_word_with_blanks = ''.join(
            guess if word[i] == guess else word_with_blanks[i]
            for i in range(len(word))
        )
        word_with_blanks = new_word_with_blanks
        label1.config(text=word_with_blanks)
        if '_' not in word_with_blanks:
            end_game("win")
    else:
        mistakes += 1
        update_hangman(mistakes)
        if mistakes == 6:
            end_game("lose")
    guess_entry.delete(0, END)

def end_game(result):
    if result == "win":
        result_text = "Congratulations You win the game....!"
    else:
        result_text = f"You lose, the word was '{word}'...!"
    result_label.config(text=result_text)

def start_new_game():
    global word, word_with_blanks, mistakes
    word = choose_word()
    word_with_blanks = '_' * len(word)
    mistakes = 0
    label1.config(text=word_with_blanks)
    canvas.delete("all")
    canvas.create_line(150, 260, 250, 260, width=3)
    canvas.create_line(200, 260, 200, 40, width=3)
    canvas.create_line(200, 90, 250, 40, width=3)
    canvas.create_line(200, 40, 300, 40, width=3)
    canvas.create_line(300, 40, 300, 70, width=3)
    result_label.config(text="",font=("Candara", 20, "bold"))
start_new_game()

root.mainloop()
