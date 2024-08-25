from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and not check_winner():
        buttons[row][column]["text"] = player

        winner = check_winner()
        if winner:
            if winner == "Tie":
                label.config(text="Tie")
            else:
                label.config(text=f"{winner} wins")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player}'s turn")

def check_winner():
    
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            color_winner(buttons[i][0], buttons[i][1], buttons[i][2])
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            color_winner(buttons[0][i], buttons[1][i], buttons[2][i])
            return buttons[0][i]['text']

    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        color_winner(buttons[0][0], buttons[1][1], buttons[2][2])
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        color_winner(buttons[0][2], buttons[1][1], buttons[2][0])
        return buttons[0][2]['text']

   
    if not empty_spaces():
        color_all_buttons("yellow")
        return "Tie"

    return False

def color_winner(button1, button2, button3):
    button1.config(bg="green")
    button2.config(bg="green")
    button3.config(bg="green")

def color_all_buttons(color):
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(bg=color)

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player}'s turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0] for _ in range(3)]

label = Label(text=f"{player}'s turn", font=("consolas", 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas", 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
