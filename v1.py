# importing modules
from tkinter import *
import re
import math

# create main_window
root = Tk()
root.title("Calculator using TKinter")
# root.geometry("300x400")?
root.resizable(False, False)

# Central input handler
def handle_input(value):
    current_text = screen.get()
    if value == '=':
        try:
            final_expression = current_text.replace('^', '**')
            final_expression = current_text.replace('π', "math.pi")
            screen.set(str(eval(final_expression)))
        except: screen.set("Error")
    elif value == 'π':
        if current_text and (current_text[-1].isdigit() or current_text[-1] == ')'):
            screen.set(current_text+'*π')
        else:
            screen.set(current_text+'π')
    elif value == 'C':
        screen.set("")
    elif value == '◀':
        current_text = current_text[0: len(current_text) - 1]
        screen.set(current_text)
    elif value == '%':
            # extract the last number using regex
            match = re.search(r'(\d+\.?\d*)$', current_text)
            if match:
                last_number = match.group(1)
                percent_value = str(float(last_number)/100)
                # replace last number with divided result
                new_text = current_text[:match.start()] + percent_value
                screen.set(new_text)
            
    elif value == '.':
        last_number = re.split(r'[+\-*/]', current_text) [-1]
        if '.' not in last_number:
            screen.set(current_text + '.')
    else:
            screen.set(current_text + value)
            
    # move cursor at end of new insetion
    entry.icursor(END)




def on_click(event):
    btn_text = event.widget['text']
    handle_input(btn_text)

# Entry field
screen = StringVar()
entry = Entry(root, textvar=screen, font='Arial 20', bd=0,
              relief=FLAT, justify='right', bg='#F0EBE3', fg='#333333')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30, sticky='nsew')
entry.focus_set()
entry.bind('<KeyPress-%>', lambda e:handle_input('%') or 'break')
entry.bind('<KeyPress>', lambda e:'break' if e.char.isalpha() else None)
entry.bind('<Return>', lambda event: handle_input('='))
entry.bind('<Delete>', lambda event: handle_input('C'))


# Buttons layout
buttons = [ 
           ['(', ')', 'C', '◀'],
           ['^', 'π', '%', '/'],
           ['7', '8', '9', '*'],
           ['4', '5', '6', '+'],
           ['1', '2', '3', '-'],
           ['0', '00','.', '=']
           ]

# create buttons using grid layout
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        # Base colors
        bg_color = '#FBFBFB'
        fg_color = '#2C2C2C'

        # Operator buttons
        if btn_text in {'/', '*', '-', '+', 'π', '%', '^'}:
            bg_color = '#F1F1F1'

        # Special buttons
        elif btn_text in {'C', '◀', '(', ')'}:
            bg_color = '#eaeaea'

        # Equals
        elif btn_text == '=':
            bg_color = '#FFEC9E'


        btn = Button(root, text=btn_text, font='Arial 18', bd=2,
                     bg=bg_color, fg=fg_color, activebackground='#dcdcdc')
        btn.grid(row=i+1, column=j, sticky='nsew', padx=2, pady=2)
        btn.bind('<Button-1>', on_click)


root.configure(bg='#F0EBE3')



        
# run application
root.mainloop()
