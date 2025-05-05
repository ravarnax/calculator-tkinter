import tkinter as tk
import re
import math

root = tk.Tk()
root.title("Windows Style Calculator")
root.geometry("360x540")
root.resizable(False, False)
root.configure(bg="#CFF2F8")
memory = 0
is_dark_mode = False  # Track theme mode

# ================== Main Input Handling ===================
def handle_input(value):
    global memory
    current_text = screen.get()
    if value == '=':
        try:
            screen.set(str(eval(current_text)))
        except:
            screen.set("Error")
            root.after(2000, lambda: screen.set(current_text), entry.icursor(tk.END))
    elif value == '¹⁄ₓ':
        last_op_match = re.search(r'[\+\-\*/](?!.*[\+\-\*/])', current_text)
        if last_op_match:
            last_op_index = last_op_match.start()
            last_num = current_text[last_op_index + 1:]
            restore_point = current_text[:last_op_index + 1]
        else:
            last_num = current_text
            restore_point = ""
        try:
            num_value = eval(last_num)
            if num_value == 0:
                screen.set("Error")
                root.after(2000, lambda: (screen.set(restore_point), entry.icursor(tk.END)))
            else:
                inverse = 1 / num_value
                new_text = restore_point + str(inverse)
                screen.set(new_text)
        except:
            screen.set("Error")
            root.after(2000, lambda: (screen.set(restore_point), entry.icursor(tk.END)))
    elif value == '²√x':
        last_num = re.split(r'[+\-*/]', current_text)[-1]
        screen.set(str(math.sqrt(float(last_num))))
    elif value == 'x²':
        last_num_match = re.search(r'(\d+\.?\d*)$', current_text)
        if last_num_match:
            last_num = last_num_match.group(1)
            square = str(math.pow(float(last_num), 2))
            new_text = current_text[:last_num_match.start()] + square
            screen.set(new_text)
        else:
            screen.set(current_text)
    elif value == 'C':
        screen.set('')
    elif value == 'CE':
        last_op_match = re.search(r'[\+\-\*\/](?!.*[\+\-\*/])', current_text)
        if last_op_match:
            last_op_index = last_op_match.start()
            new_text = current_text[:last_op_index + 1]
            screen.set(new_text)
        else:
            screen.set('')
    elif value == '⌫':
        screen.set(current_text[:len(current_text) - 1])
    elif value == "%":
        last_num_match = re.search(r'(\d+\.?\d*)$', current_text)
        if last_num_match:
            last_num = last_num_match.group(1)
            percent_value = str(float(last_num) / 100)
            new_text = current_text[:last_num_match.start()] + percent_value
            screen.set(new_text)
    elif value == '⁺⁄₋':
        last_num_match = re.search(r'(\(-?(?:\d+\.?\d*|\.\d+)\)|(?:\d+\.?\d*|\.\d+))$', current_text)
        if last_num_match:
            last_num = last_num_match.group(1)
        if last_num.startswith('(-') and last_num.endswith(')'):
            new_text = last_num[2:-1]
        else:
            new_text = f'(-{last_num})'
        screen.set(current_text[:last_num_match.start()] + new_text)
    elif value == '.':
        last_num = re.split(r'[\+\-\*/\(\)]', current_text)[-1]
        if '.' not in last_num:
            screen.set(current_text + '.')
    elif value in ('MC', 'MR', 'M+', 'M-', 'MS'):
        if value == 'MC':
            memory = 0
        elif value == 'MR':
            mem_str = str(memory)
            last_op_match = re.search(r'[\+\-\*\/](?!.*[\+\-\*/])', screen.get())
            if last_op_match:
                last_op_index = last_op_match.start()
                if last_op_index == 0:
                    new_text = mem_str
                else:
                    new_text = current_text[:last_op_index + 1] + mem_str
            else:
                new_text = mem_str
            screen.set(new_text)
        elif value == 'M+':
            memory += float(current_text.replace('−', '-'))
        elif value == 'M-':
            memory -= float(current_text.replace('−', '-'))
        elif value == 'MS':
            current_text = screen.get()
            try:
                memory = float(current_text.replace('−', '-'))
            except ValueError:
                pass
        return
    else:
        screen.set(current_text + value)
    entry.icursor(tk.END)

# ================== Theme Toggle ===================
def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    if is_dark_mode:
        dark_bg = "#146551"
        root.configure(bg=dark_bg)
        mem_frame.configure(bg=dark_bg)
        entry.configure(bg="#8FC1B5", fg="#f0f0f0", insertbackground="#265C4B")
        theme_btn.configure(text='☀️', bg=dark_bg, fg="#f0f0f0")
        for btn in mem_buttons_list:
            btn.configure(
                bg=dark_bg,
                fg="#f0f0f0",
                activebackground="#3a3a3a",
                activeforeground="#f0f0f0",
                bd=0,
                highlightthickness=0,
                relief="flat"
            )
        for btn in calc_buttons_list:
            if btn == equal_btn: 
                btn.configure(
                    bg="#16575A",
                    fg="#ffffff",
                    activebackground="#259095",
                    activeforeground="#ffffff",
                    bd=0,
                    highlightthickness=0,
                    relief="flat"
                )
            # elif btn == backspace_btn:
            #     btn.configure(bg='#F20505')
            else:
                btn.configure(
                    bg=dark_bg,
                    fg="#f0f0f0",
                    activebackground="#3a3a3a",
                    activeforeground="#f0f0f0",
                    bd=0,
                    highlightthickness=0,
                    relief="flat"
                )
    else:
        root.configure(bg="#CFF2F8")
        mem_frame.configure(bg="#CFF2F8")
        entry.configure(bg="white", fg="black", insertbackground="black")
        theme_btn.configure(text='🌙', bg="#CFF2F8", fg="black")
        for btn in mem_buttons_list:
            btn.configure(
                bg="#CFF2F8",
                fg="black",
                activebackground="#e6e6e6",
                activeforeground="black",
                bd=0,
                highlightthickness=0,
                relief="flat"
            )
        for btn in calc_buttons_list:
            if btn == equal_btn:  
                btn.configure(
                    bg="#36DAE2",
                    fg="#ffffff",
                    activebackground="#36cad1",
                    activeforeground="#ffffff",
                    bd=0,
                    highlightthickness=0,
                    relief="flat"
                )
            # elif btn == backspace_btn:
            #     btn.configure(bg='#F28705')
            else:
                btn.configure(
                    bg="#CFF2F8",
                    fg="black",
                    activebackground="#e6e6e6",
                    activeforeground="black",
                    bd=0,
                    highlightthickness=0,
                    relief="flat"
                )


# ================== Setup UI ===================
def on_click(event):
    btn_text = event.widget['text']
    handle_input(btn_text)

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font='Arial 22', relief=tk.FLAT, bg='white', fg='black', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30, sticky='nsew')
entry.focus_set()

# Theme toggle button
theme_btn = tk.Button(root, text="🌙", command=toggle_theme, bg="#CFF2F8", bd=0, font=("Arial", 12))
theme_btn.place(x=325, y=2)

# Memory button frame
mem_frame = tk.Frame(root, bg="#CFF2F8")
mem_frame.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=8, pady=4)

memory_buttons = ['MC', 'MR', 'M+', 'M-', 'MS']
mem_buttons_list = []
for text in memory_buttons:
    btn = tk.Button(mem_frame, text=text, font=("Arial", 10), bg="#CFF2F8", fg="black", bd=0,
                    activebackground="#e6e6e6")
    btn.pack(side="left", expand=True, fill="both", padx=2)
    btn.bind("<Button-1>", on_click)
    mem_buttons_list.append(btn)

# Calculator buttons
buttons = [
    ['%', 'CE', 'C', '⌫'],
    ['¹⁄ₓ', 'x²', '²√x', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '−'],
    ['1', '2', '3', '+'],
    ['±', '0', '.', '=']
]
calc_buttons_list = []
equal_btn = None

for r, row in enumerate(buttons, start=2):
    for c, char in enumerate(row):
        btn = tk.Button(root, text=char, font=("Arial", 14), bg="#CFF2F8", fg="black", bd=0,
                        activebackground="#e6e6e6")
        btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
        btn.bind('<Button-1>', on_click)
        calc_buttons_list.append(btn)
        if char == '=':
            btn.config(bg="#36DAE2")
            equal_btn = btn  

# Responsive grid
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(9):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
