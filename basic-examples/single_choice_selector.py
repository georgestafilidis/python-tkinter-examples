import tkinter as tk

def show_selection():
    label.config(text=f"Choice: {var.get()}")

root = tk.Tk()
root.title("RadioButtons")
root.geometry("400x400")

var = tk.StringVar(value="No Choice")

radio1 = tk.Radiobutton(root, text="Male", variable=var, value="Male", command=show_selection)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Female", variable=var, value="Female", command=show_selection)
radio2.pack()

radio3 = tk.Radiobutton(root, text="Other", variable=var, value="Other", command=show_selection)
radio3.pack()

label = tk.Label(root, text="No Choice", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()
