# import modules
from tkinter import *

# create main window
root = Tk()
root.geometry('300x400')
root.title("Calculator v01")
root.resizable(False, False)

# handle inputs
def handle_input(value):
    current_text = screen.get()
    if value == '=':
        try:
            screen.set(str(eval(current_text)))
        except:
            screen.set("Error")
    elif value == 'C':
        screen.set('')
    else:
        screen.set(current_text+value)
        
    # move the cursor at the end of new text insertion
    entry.icursor(END)

# handle mouse event
def on_click(event):
    btn_text = event.widget['text']
    handle_input(btn_text)
    
# handle keyboard input (Enter key)
def on_enter(event):
    handle_input('=')
    

# Create Entry field
screen = StringVar()
entry = Entry(root, textvar=screen, font='Helvetica 20', bd=10, relief=RIDGE, justify='right')
entry.pack(fill='both', padx=10, pady=10, ipadx=8)
entry.focus_set()   # direct focus to the widget   

entry.bind("<Return>", on_enter)

# button layout
buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['C', '0', '=', '+']]

# create buttons and pack buttons
for row in buttons:
    frame = Frame(root)
    frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = Button(frame, text=btn_text, font='Helvetica 20', bd=5)
        btn.pack(side='left', expand=True, fill='both')
        btn.bind("<Button-1>", on_click)

# run application
root.mainloop()
