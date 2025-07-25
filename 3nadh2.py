import tkinter as tk
from tkinter import ttk, messagebox

class PlayerScoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Players Scoring")

        # Data: dictionary with sport categories mapping to list of (player, score)
        self.data = {
            "Football": [],
            "Basketball": [],
            "Tennis": [],
            "Cricket": [],
            "Badminton": []
        }

        # Sport selection
        ttk.Label(root, text="Select Sport Category:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.sport_var = tk.StringVar()
        self.sport_combo = ttk.Combobox(root, textvariable=self.sport_var, values=list(self.data.keys()), state="readonly")
        self.sport_combo.grid(row=0, column=1, padx=10, pady=5)
        self.sport_combo.current(0)
        self.sport_combo.bind("<<ComboboxSelected>>", self.update_player_list)

        # Player name entry
        ttk.Label(root, text="Player Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = ttk.Entry(root)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Player score entry
        ttk.Label(root, text="Player Score:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.score_entry = ttk.Entry(root)
        self.score_entry.grid(row=2, column=1, padx=10, pady=5)

        # Add player button
        self.add_button = ttk.Button(root, text="Add Player", command=self.add_player)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Players listbox with scrollbar
        self.players_listbox = tk.Listbox(root, width=40, height=10)
        self.players_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.players_listbox.yview)
        self.scrollbar.grid(row=4, column=2, sticky='ns')
        self.players_listbox.config(yscrollcommand=self.scrollbar.set)

        self.update_player_list()

    def add_player(self):
        sport = self.sport_var.get()
        name = self.name_entry.get().strip()
        score_text = self.score_entry.get().strip()

        if not name:
            messagebox.showwarning("Input Error", "Please enter a player name.")
            return

        if not score_text.isdigit():
            messagebox.showwarning("Input Error", "Score must be a positive integer.")
            return

        score = int(score_text)
        self.data[sport].append((name, score))

        # Clear inputs
        self.name_entry.delete(0, tk.END)
        self.score_entry.delete(0, tk.END)

        self.update_player_list()

    def update_player_list(self, event=None):
        sport = self.sport_var.get()
        self.players_listbox.delete(0, tk.END)
        players = self.data.get(sport, [])
        if players:
            for idx, (name, score) in enumerate(players, start=1):
                self.players_listbox.insert(tk.END, f"{idx}. {name} - Score: {score}")
        else:
            self.players_listbox.insert(tk.END, "No players added for this sport yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlayerScoreApp(root)
    root.mainloop()
