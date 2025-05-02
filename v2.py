# practise calculator
from tkinter import *
import math
import re
import time


# main_window
root = Tk()
root.title("Calculator")
root.resizable(False, False)

# functions
# Central input handle function
def handle_input(value):
    current_text = screen.get()
    if value == '=':
        try:
            screen.set(str(eval(current_text)))
        except:
            screen.set("Error")
            root.after(2000, lambda: screen.set(current_text), entry.icursor(END))
            
    elif value == '¹⁄ₓ':  # Inverse (1/x) button pressed
        last_op_match = re.search(r'[\+\-\*/](?!.*[\+\-\*/])', current_text)

        if last_op_match:
            last_op_index = last_op_match.start()
            last_num = current_text[last_op_index + 1:]  # Get part after last operator
            restore_point = current_text[:last_op_index + 1]
        else:
            last_num = current_text
            restore_point = current_text  # Restore full input if no operator

        try:
            num_value = eval(last_num)
            if num_value == 0:
                screen.set("Error")
                root.after(2000, lambda: (screen.set(restore_point), entry.icursor(END)))
            else:
                inverse = 1 / num_value
                new_text = restore_point + str(inverse)
                screen.set(new_text)
        except:
            screen.set("Error")
        root.after(2000, lambda: (screen.set(restore_point), entry.icursor(END)))

    elif value == '√x':
        last_num = re.split(r'[+\-*/]', current_text)[-1]
        screen.set(str(math.sqrt(float(last_num))))
    
    elif value == 'x²':
            last_num_match = re.search(r'(\d+\.?\d*)$', current_text)
            if last_num_match: 
                last_num = last_num_match.group(1)
                square = str(math.pow(float(last_num),2))
                # replace last number with divided result
                new_text = current_text[:last_num_match.start()] + square
                screen.set(new_text)
            else:
                screen.set(current_text+value)        
    elif value == 'C':
        screen.set('')
    
    elif value == 'CE': # clear last number after Operator
        last_op_match = re.search(r'[\+\-\*\/](?!.*[\+\-\*/])', current_text)
        if last_op_match:
            last_op_index = last_op_match.start()
            new_text = current_text[:last_op_index+1] # keep everything upto last operator
            screen.set(new_text)
        else:
            # No operator ? clear everything (same as C)
            screen.set("")
        
    elif value == '⌫':
        screen.set(current_text[:len(current_text)-1])
        
    elif value == '%':
        last_num_match = re.search(r'(\d+\.?\d*)$', current_text)
        if last_num_match: 
            last_num = last_num_match.group(1)
            percent_value = str(float(last_num)/100)
            # replace last number with divided result
            new_text = current_text[:last_num_match.start()] + percent_value
            screen.set(new_text)
    
    elif value == "⁺⁄₋":
        # Match a number possibly already wrapped in (- ... )
            last_num_match = re.search(r'(\(-?(?:\d+\.?\d*|\.\d+)\)|(?:\d+\.?\d*|\.\d+))$', current_text)       
            if last_num_match:
                last_num = last_num_match.group(1)

            if last_num.startswith('(-') and last_num.endswith(')'):
                # It's already negative in brackets → remove the brackets
                new_text = last_num[2:-1]  # remove '(-' and ')'
            else:
                # It's positive → wrap in (- ...)
                new_text = f'(-{last_num})'

            screen.set(current_text[:last_num_match.start()] + new_text)
        # entry.icursor(END)
        
    elif value == '.':
        # Split by operators to get the last "number part"
        last_num = re.split(r'[\+\-\*/\(\)]', current_text)[-1]
        if '.' not in last_num:
            screen.set(current_text + '.')



        
    else:
        screen.set(current_text+value)
    entry.icursor(END)

def on_click(event):
    btn_text = event.widget['text']
    handle_input(btn_text)

# entry field
screen = StringVar()
entry = Entry(root, textvar=screen, font='Arial 20', bd=0, relief=FLAT, justify='right', bg='#F0EBE3')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30, sticky='nsew')
entry.focus_set()
entry.bind('<Return>', lambda event: handle_input('='))
entry.bind('<Delete>', lambda event: handle_input('C'))
entry.bind('<KeyPress-%>', lambda e: handle_input('%') or 'break')
entry.bind('<KeyPress-.>', lambda e: handle_input('.') or 'break')

entry.bind('<KeyPress>', lambda e: 'break' if e.char.isalpha() else None)

# button section
# button layout
buttons = [
          ['%', 'CE', 'C', '⌫'],
          ['¹⁄ₓ', 'x²', '√x', '÷'],
          ['7', '8', '9', '×'],
          ['4', '5', '6', '-'],
          ['1', '2', '3', '+'],
          ['⁺⁄₋', '0', '.', '=']
]

# create buttons using grid layout
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        # base colors
        bg_color = '#fbfbfb'
        fg_color = '#2c2c2c'
                
        # operator buttons 
        if btn_text in {'/', '*', '-', '+'}:
            bg_color = '#f1f1f1'
        
        # special buttons 
        elif btn_text in {'%', 'CE', 'C', '⌫'}:
            bg_color = '#eaeaea'
            
        # equals 
        elif btn_text == '=':
            bg_color = "#ffec9e"
        
        btn = Button(root, text=btn_text, font='Arial 18', bd=2, 
                     bg=bg_color, fg=fg_color, activebackground='#dcdcdc')
        btn.grid(row=i+1, column=j, sticky='nsew', padx=2, pady=2)
        btn.bind('<Button-1>', on_click)
        
root.configure(bg='#f0ebe3')

# run application
root.mainloop()
        
