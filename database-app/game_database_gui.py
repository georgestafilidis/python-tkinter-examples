import tkinter as tk
from tkinter import messagebox
from db_connection import get_connection

def insert_game(title, genre, release_year):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO Games (title, genre, release_year) VALUES (%s, %s, %s)"
        values = (title, genre, release_year)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print("Σφάλμα: ", e)
        return False

def fetch_games():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "SELECT id, title, genre, release_year FROM Games"
        cursor.execute(sql)
        games = cursor.fetchall()
        cursor.close()
        connection.close()
        return games
    except Exception as e:
        print("Σφάλμα κατά την ανακτηση", e)
        return []

def submit_game():
    title = entry_title.get()
    genre = entry_genre.get()
    year = entry_year.get()

    if not (title and genre and year):
        messagebox.showwarning("Σφάλμα", "Συμπληρώστε όλα τα πεδία!")
        return

    try:
        year = int(year)
    except ValueError:
        messagebox.showerror("Σφάλμα", "Το έτος πρέπει να είναι αριθμός!")
        return

    if insert_game(title, genre, year):
        messagebox.showinfo("Επιτυχία", "Το παιχνίδι προστέθηκε επιτυχώς!")
    else:
        messagebox.showerror("Αποτυχία", "Αποτυχία εισαγωγής παιχνιδιού!")

def show_games():
    games = fetch_games()
    listbox.delete(0, tk.END) 
    if games:
        for game in games:
            listbox.insert(tk.END, f"{game[1]} - {game[2]} - {game[3]}")
    else:
        listbox.insert(tk.END, "Δεν υπάρχουν καταχωρημένα παιχνίδια.")

root = tk.Tk()
root.title("Game Database")

label_title = tk.Label(root, text="Τίτλος Παιχνιδιού:")
label_title.grid(row=0, column=0, padx=10, pady=5)

entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1, padx=10, pady=5)

label_genre = tk.Label(root, text="Είδος Παιχνιδιού:")
label_genre.grid(row=1, column=0, padx=10, pady=5)

entry_genre = tk.Entry(root)
entry_genre.grid(row=1, column=1, padx=10, pady=5)

label_year = tk.Label(root, text="Έτος Κυκλοφορίας:")
label_year.grid(row=2, column=0, padx=10, pady=5)

entry_year = tk.Entry(root)
entry_year.grid(row=2, column=1, padx=10, pady=5)

button_submit = tk.Button(root, text="Προσθήκη Παιχνιδιού", command=submit_game)
button_submit.grid(row=3, column=0, columnspan=2, pady=10)

button_show = tk.Button(root, text="Προβολή Παιχνιδιών", command=show_games)
button_show.grid(row=4, column=0, columnspan=2, pady=10)

listbox = tk.Listbox(root, width=50, height=10)
listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
