import tkinter as tk
root = tk.Tk()
root.title("Frame")
root.geometry("300x400")

frame1 = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame1.pack(pady=10)

label1 = tk.Label(frame1, text="Type something:", font=("Arial", 14))
label1.pack()

entry = tk.Entry(frame1, font=("Arial", 12))
entry.pack()

frame2 = tk.Frame(root, bg="silver", padx=10, pady=10)
frame2.pack(pady=10)
def show_text():
    result = entry.get()
    label2.config(text=f"Result: {result}")

button = tk.Button(frame2, text="Show", command=show_text)
button.pack()

label2 = tk.Label(frame2, text="Result:", font=("Arial", 14))
label2.pack()

root.mainloop()
