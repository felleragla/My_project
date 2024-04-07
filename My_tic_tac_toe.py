import tkinter as tk

current_player = 1
size = 3
winner_label = None
size_entry = None
buttons = None

def check_winner(symbol):
    for i in range(size):
        if all(buttons[i][j]['text'] == symbol for j in range(size)) or \
           all(buttons[j][i]['text'] == symbol for j in range(size)):
            return True

    if all(buttons[i][i]['text'] == symbol for i in range(size)) or \
       all(buttons[i][size - 1 - i]['text'] == symbol for i in range(size)):
        return True

    return False

def ButtonClick(row, col):
    global current_player
    print("Position cliquée:", row, col)

    
    if buttons[row][col]['text'] == ' ':
        symbol = "p" if current_player == 1 else "o"
        buttons[row][col]['text'] = symbol
        if check_winner(symbol):
            show_winner_message(f"Le joueur {current_player} a gagné!")
        elif all(buttons[i][j]['text'] != ' ' for i in range(size) for j in range(size)):
            show_winner_message("Match nul!")
        else:
            current_player = 2 if current_player == 1 else 1

def on_click(row, col):
    ButtonClick(row, col)

def restart_game():
    global current_player, winner_label
    if winner_label:
        winner_label.destroy()
    current_player = 1
    create_game_board()

def show_winner_message(message):
    global winner_label
    if winner_label is None:
        winner_label = tk.Label(root, text=message, font=("Helvetica", 12))
        winner_label.grid(row=size + 1, column=0, columnspan=size)
    else:
        winner_label.config(text=message)

def create_game_board():
    global buttons
    for widget in root.winfo_children():
        widget.destroy()

    buttons = [[None] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            buttons[i][j] = tk.Button(root, text=' ', width=5, height=2,
                                       command=lambda row=i, col=j: on_click(row, col))
            buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

    restart_button = tk.Button(root, text="Restart", command=restart_game)
    restart_button.grid(row=size + 2, column=0, columnspan=size, pady=5)

def start_game():
    global size
    try:
        size = int(size_entry.get())
        if size < 3:
            raise ValueError("La taille doit être au moins de 3.")
        create_game_board()
    except ValueError:
        show_winner_message("La taille doit être un nombre entier supérieur ou égal à 3.")

root = tk.Tk()
root.title("Jeu Tic Tac Toe")

size_entry_label = tk.Label(root, text="Taille de la table de jeu:")
size_entry_label.grid(row=0, column=0, pady=5)
size_entry = tk.Entry(root)
size_entry.insert(0, str(size))
size_entry.grid(row=0, column=1, pady=5)

start_button = tk.Button(root, text="Démarrer le jeu", command=start_game)
start_button.grid(row=1, column=0, columnspan=2, pady=5)

root.mainloop()