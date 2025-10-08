import tkinter as tk
from tkinter import messagebox 
window = tk.Tk() 
field = []
for i in range(9):
    field.append(' ') #append - добавляет в конец списка элемент, который указан в кавычках. т. е. цикл 9 раз повторяется и каждый раз пробел добавляется 
current_player = 'X'
buttons = []
start_button = None
def create_field():
    window.title("Крестики-Нолики")
    for i in range(3):
        for j in range(3):
            index = 3 * i + j
            button = tk.Button(window, text='', font=('Arial', 20), 
                               width=10, height=5,
                             command=lambda idx=index: make_move(idx),
                             bg="#C7D68C",
                             fg="#AD3131",
                             relief='sunken', borderwidth=3,
                             activebackground="#242285")
                             
            button.grid(row=i+1, column=j)
            buttons.append(button)
def make_move(index):
    global current_player
    if field[index] == ' ' and current_player == 'X':
        field[index] = 'X'
        buttons[index].config(text='X', state='disabled')
        if not check_winner():
            current_player = 'O'
            bot_move()
def bot_move():
    global current_player
    for i in range(9):
        if field[i] == ' ':
            field[i] = 'O'
            if check_winner_bot() == 'O':
                buttons[i].config(text='O', state='disabled')
                check_winner()
                current_player = 'X'
                return
            field[i] = ' '
    for i in range(9):
        if field[i] == ' ':
            field[i] = 'X'
            if check_winner_bot() == 'X':
                field[i] = 'O'
                buttons[i].config(text='O', state='disabled')
                check_winner()
                current_player = 'X'
                return
            field[i] = ' '
    for move in [4, 0, 2, 6, 8, 1, 3, 5, 7]:  
        if field[move] == ' ':
            field[move] = 'O'
            buttons[move].config(text='O', state='disabled')
            break
    check_winner()
    current_player = 'X'
def check_winner_bot():
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if field[a] == field[b] == field[c] != ' ':
            return field[a]
    return 'tie' if ' ' not in field else None
def check_winner():
    winner = check_winner_bot()
    if winner == 'X':
        messagebox.showinfo("Победа!", "Вы победили!")
        reset_game()
        return True
    elif winner == 'O':
        messagebox.showinfo("Поражение", "Бот победил!")
        reset_game()
        return True
    elif winner == 'tie':
        messagebox.showinfo("Ничья", "Игра закончилась вничью!")
        reset_game()
        return True
    return False
def reset_game():
    global field, current_player
    field = []
    for i in range(9):
        field.append(' ')
    current_player = 'X'
    for button in buttons:
        button.config(text='', state='normal')
def main():
    create_field()
    window.mainloop()
if __name__ == "__main__":
    main()
