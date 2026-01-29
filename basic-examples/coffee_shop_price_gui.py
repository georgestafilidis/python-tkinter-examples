import tkinter as tk

def calculate_price():
    price = 0
    coffee = coffee_var.get()
    if coffee == "Espresso":
        price = 2
    elif coffee == "Cappuccino":
        price = 3
    elif coffee == "Latte":
        price = 3.5

    # Add sugar/milk if selected
    if sugar_var.get():
        price += 0.5
    if milk_var.get():
        price += 0.5

    label_result.config(text=f"Total Price: €{price:.2f}")

root = tk.Tk()
root.title("Coffee Order")
root.geometry("400x400")

tk.Label(root, text="Choose your coffee:", font=("Arial", 12)).pack()
coffee_var = tk.StringVar(value="Espresso")

tk.Radiobutton(root, text="Espresso (€2)", variable=coffee_var, value="Espresso").pack()
tk.Radiobutton(root, text="Cappuccino (€3)", variable=coffee_var, value="Cappuccino").pack()
tk.Radiobutton(root, text="Latte (€3.5)", variable=coffee_var, value="Latte").pack()

tk.Label(root, text="Choose cup size:", font=("Arial", 12)).pack()
size_var = tk.StringVar(value="Small")
tk.Radiobutton(root, text="Small", variable=size_var, value="Small").pack()
tk.Radiobutton(root, text="Big", variable=size_var, value="Big").pack()

tk.Label(root, text="Extras:", font=("Arial", 12)).pack()
sugar_var = tk.BooleanVar()
milk_var = tk.BooleanVar()

tk.Checkbutton(root, text="Add Sugar (+€0.5)", variable=sugar_var).pack()
tk.Checkbutton(root, text="Add Milk (+€0.5)", variable=milk_var).pack()

tk.Button(root, text="Calculate Price", command=calculate_price).pack(pady=10)
label_result = tk.Label(root, text="Total Price: €0.00", font=("Arial", 14))
label_result.pack()

root.mainloop()
