import tkinter as tk

root = tk.Tk()
root.title("label Demo")
root.geometry("600x200")

greeting = tk.Label(
    root,
    text="Welcome Student 26628503, Jack Armstrong",
    font=("Courier", 14, "italic"),
    fg="navy",
    bg="lightyellow",
)
second_greeting = tk.Label(
    root,
    text="CIS1703 Proramming Lab",
    font=("Courier", 14, "italic"),
    fg="pink",
    bg="black",
)
greeting.pack(pady=40)
second_greeting.pack(pady=40)
root.mainloop()