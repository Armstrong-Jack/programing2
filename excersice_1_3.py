import tkinter as tk
total_amounts_clicked = 0
def on_button_click():
    global total_amounts_clicked
    total_amounts_clicked += 1
    output_label.config(text=f"Button Was Clicked! {total_amounts_clicked} times")

def on_button_click_reset():
    global total_amounts_clicked
    total_amounts_clicked  = 0
    output_label.config(text="Button clicked was reset!")


root = tk.Tk()
root.title("Button Demo")
root.geometry("400x200")

my_button = tk.Button(
    root,
    text="Click Me",
    command=on_button_click,
    font=("Arial,14"),
    fg= "pink",
    bg="blue"
)

my_reset_button = tk.Button(
    root,
    text="reset",
    command=on_button_click_reset,
    font=("Arial,14"),
    fg= "pink",
    bg="blue"
)

my_button.pack(pady=20)
my_reset_button.pack(pady=1)
output_label = tk.Label(root, text="", font=("Arial", 14))
output_label.pack()
root.mainloop()