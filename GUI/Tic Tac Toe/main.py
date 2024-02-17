import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple


class Move(NamedTuple):
    row: int
    col: int
    label: str = ""
    
    
class Player(NamedTuple):
    label: str
    color: str


FONT = ("Verdana", 25)   
PLAYERS = (
    Player(label='X', color='RoyalBlue'),
    Player(label='O', color='SandyBrown'),
)


class Game:
    
    def __init__(self, players=PLAYERS):
        self.players = cycle(players)
        self.board_size = 3
        self.current_player = next(self.players)
        self.current_moves = []
        self.winner_combo = []
        self.winning_combos = []
        self.game_winner = False
        self.board_setup()
        
    def board_setup(self):

        self.current_moves = [[Move(row, col) for row in range(self.board_size)] for col in range(self.board_size)]
        self.winning_combos = self.get_winning_combos()
        
    def get_winning_combos(self):
        return [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], 
                [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)], 
                [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], 
                [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
			
    def is_valid_move(self, move):
        """Return True if move is valid, and False otherwise."""
        row, col = move.row, move.col
        move_was_not_played = self.current_moves[row][col].label == ""
        no_winner = not self.game_winner
        return no_winner and move_was_not_played         
    
    def process_move(self, move):
        """Process the current move and check if it's a win."""
        row, col = move.row, move.col
        self.current_moves[row][col] = move
        for combo in self.winning_combos:
            results = set(self.current_moves[n][m].label for n, m in combo)
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self.game_winner = True
                self.winner_combo = combo
                break
            
    def has_winner(self):
        """Return True if the game has a winner, and False otherwise."""
        return self.game_winner
    
    def is_tied(self):
        """Return True if the game is tied, and False otherwise."""
        no_winner = not self.game_winner
        played_moves = (move.label for row in self.current_moves for move in row)
        return no_winner and all(played_moves)
    
    def toggle_player(self):
        """Return a toggled player."""
        self.current_player = next(self.players)
        
 
class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        container = tk.Frame(self)
        container.pack(padx=10, pady=10, side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
		# iterating through a tuple consisting
		# of the different page layouts
        for page in (StartPage, StartGame):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(StartPage)
            menubar = self.menubar()
            self.configure(menu=menubar)
            
    def show_frame(self, page_name):
        """Show a frame for a given page name."""
        frame = self.frames[page_name]
        frame.tkraise()
           
    def menubar(self):
        menubar = tk.Menu(self)
        page_menu = tk.Menu(menubar)
        page_menu.add_command(label="New Game", command=lambda: self.new_game())
        page_menu.add_separator()
        page_menu.add_command(label='Exit', command=self.quit)
        menubar.add_cascade(label="File", menu=page_menu)
        return menubar
        
    def new_game(self):
        self.destroy()
        App()


class StartPage(tk.Frame):
    def __init__(self, parent, page_name):
        super().__init__(parent)
        label = tk.Label(self, text="-->Welcome to Tic-Tac-Toe<--", font=FONT, bg="white", fg="black")
        label.pack(padx=10, pady=10)
        button1 = tk.Button(self, text="Start Game", font=FONT, command=lambda : page_name.show_frame(StartGame))
        button1.pack(padx=10, pady=10)
        button2 = tk.Button(self, text="Exit", font=FONT, command=self.quit)
        button2.pack(padx=10, pady=10)
        
    def quit(self) -> None:
        return super().quit()
          

class StartGame(tk.Frame):
    def __init__(self, parent, page_name):
        super().__init__(parent)
        self.cells = {}
        self.game = Game()
        self.create_board_display()
        self.create_board_grid()
    
    def create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text='Ready?',
            font=font.Font(size=30, weight='bold'),
        )
        self.display.pack()  
         
    def create_board_grid(self):
        # Creating the grid frame inside the main display frame
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self.game.board_size):
            self.rowconfigure(row, weight=1, minsize=100)
            
            for col in range(self.game.board_size):
                self.columnconfigure(col, weight=1, minsize=100)
            
        # Creates an independent buttons for each button when pressed
                button = tk.Button(
                    master=grid_frame,
                    text='',
                    font=font.Font(size=36, weight='bold'),
                    fg='black',
                    width=3,
                    height=2,
                    highlightbackground='light yellow',
                )
                self.cells[button] = (row, col)
                button.bind('<ButtonPress-1>', self.play)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky='nsew'
                )     
    
    def play(self, event):
        """Handle a player's move."""
        clicked_btn = event.widget
        row, col = self.cells[clicked_btn]
        move = Move(row, col, self.game.current_player.label)
        if self.game.is_valid_move(move):
            self.update_button(clicked_btn)
            self.game.process_move(move)
            if self.game.is_tied():
                self._update_display(msg='Tied game!', color='red')
            elif self.game.has_winner():
                self._highlightcells()
                msg = f"Player {self.game.current_player.label} Win!"
                color = self.game.current_player.color
                self._update_display(msg, color)
            else:
                self.game.toggle_player()
                msg = f"{self.game.current_player.label}'s turn"
                self._update_display(msg)
                
    def update_button(self, clicked_btn):
        clicked_btn.config(text=self.game.current_player.label)
        clicked_btn.config(fg=self.game.current_player.color)
        
    def _update_display(self, msg, color='black'):
        self.display['text'] = msg
        self.display['fg'] = color
    
    def _highlightcells(self):
        for button, coordinates in self.cells.items():
            if coordinates in self.game.winner_combo:
                button.config(highlightbackground='red')

def main():
    window = App()
    window.mainloop()

if __name__=='__main__':
    main()
    