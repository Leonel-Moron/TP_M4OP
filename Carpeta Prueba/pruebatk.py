import tkinter as tk

def retrieve_input():
    text = form.get('1.0','end-1c')
    return text

window = tk.Tk()
window.geometry('400x400')
window.title("First App")
window.configure(bg='#856ff3')

lbl = tk.Label(window, text = "Input:", anchor = 'w')
lbl.grid(column = 0, row = 0)

form = tk.Text(window, width = 50, height = 20)
form.grid(column = 0, row = 1)

button_1 = tk.Button(window, bg = 'green', text = 'Save to Variable "text"', command = retrieve_input)
button_1.grid(column = 0, row = 2)

window.mainloop()