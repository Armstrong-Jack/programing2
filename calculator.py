import tkinter as tk

diget_entered_1st = 0
symbol_entered = ""
diget_entered_2nd = 0
count = 0
def enter_number(number):
    global diget_entered_1st
    global symbol_entered
    global diget_entered_2nd
    global count

    if count == 0:
        output_label.config(text="")
        diget_entered_1st = number
    elif count == 1:
        symbol_entered = number
    elif count == 2:
        diget_entered_2nd = number
        if symbol_entered == "-":
            outputed_number = diget_entered_1st - diget_entered_2nd
        elif symbol_entered == "+":
            outputed_number = diget_entered_1st + diget_entered_2nd
        elif symbol_entered == "*":
            outputed_number = diget_entered_1st * diget_entered_2nd
        elif symbol_entered =="/":
            outputed_number = diget_entered_1st / diget_entered_2nd
        else:
            outputed_number = "please enter a symbol as the second entered value"
        output_label.config(text=f" {outputed_number}")
        diget_entered_1st = 0
        symbol_entered = ""
        diget_entered_2nd = 0
        count = 0
        return
        
    count += 1




    

root = tk.Tk()
root.title("Calculator")
root.geometry("600x600")



tk.Label(
    root,
    text="numbers",
    font=("Arial",12)
    ).pack(pady=(20))
button_0 = tk.Button(
    root,
    text="0",
    command= lambda: enter_number(0),
)
button_1 = tk.Button(
    root,
    text="1",
    command= lambda: enter_number(1),
)
button_2= tk.Button(
    root,
    text="2",
    command= lambda: enter_number(2),
)
button_3= tk.Button(
    root,
    text="3",
    command= lambda: enter_number(3),
)
button_4= tk.Button(
    root,
    text="4",
    command= lambda: enter_number(4),
)
button_5= tk.Button(
    root,
    text="5",
    command= lambda: enter_number(5),
)
button_6= tk.Button(
    root,
    text="6",
    command= lambda: enter_number(6),
)
button_7= tk.Button(
    root,
    text="7",
    command= lambda: enter_number(7),
)
button_8= tk.Button(
    root,
    text="8",
    command= lambda: enter_number(8),
)
button_9= tk.Button(
    root,
    text="9",
    command= lambda: enter_number(9),
)
button_10= tk.Button(
    root,
    text="10",
    command= lambda: enter_number(10),
)
button_sub = tk.Button(
    root,
    text="-",
    command= lambda: enter_number("-"),
)
button_add = tk.Button(
    root,
    text="+",
    command= lambda: enter_number("+"),
)
button_times = tk.Button(
    root,
    text="*",
    command= lambda: enter_number("*"),
)
button_div = tk.Button(
    root,
    text="/",
    command= lambda: enter_number("/"),
)
output_label = tk.Label(root, text="", font=("Arial", 14))
output_label.pack()
button_0.pack(pady=("1"))
button_1.pack(pady=("1"))
button_2.pack(pady=("1"))
button_3.pack(pady=("1"))
button_3.pack(pady=("1"))
button_4.pack(pady=("1"))
button_5.pack(pady=("1"))
button_6.pack(pady=("1"))
button_7.pack(pady=("1"))
button_8.pack(pady=("1"))
button_9.pack(pady=("1"))
button_10.pack(pady=("1"))
button_add.pack(pady=("1"))
button_sub.pack(pady=("1"))
button_times.pack(pady=("1"))
button_div.pack(pady=("1"))

root.mainloop()