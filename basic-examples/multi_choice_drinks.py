import tkinter as tk

def show_selection():
    selected = []

    if var1.get():
        selected.append("Coffee")
    if var2.get():
        selected.append("Tea")
    if var3.get():
        selected.append("Juice")

    label.config(text=f"Choices: {', '.join(selected)}")

root = tk.Tk()
root.title("CheckButtons")
root.geometry("400x400")

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

chk1 = tk.Checkbutton(root, text="Coffee", variable=var1, command=show_selection)
chk1.pack()

chk2 = tk.Checkbutton(root, text="Tea", variable=var2, command=show_selection)
chk2.pack()

chk3 = tk.Checkbutton(root, text="Juice", variable=var3, command=show_selection)
chk3.pack()

label = tk.Label(root, text="Choices:")
label.pack(pady=10)

root.mainloop()
