import tkinter as tk

def click(text):
    current_text = output_display.get("1.0", tk.END).strip()
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, current_text + text)

def calculate():
    try:
        expression = output_display.get("1.0", tk.END).strip()
        result = eval(expression)
        if len(str(result)) > 10:
            result = "{:.5e}".format(result)
        output_display.delete("1.0", tk.END)
        output_display.insert(tk.END, str(result))
    except Exception as e:
        output_display.delete("1.0", tk.END)
        output_display.insert(tk.END, "Error")

def clear():
    output_display.delete("1.0", tk.END)

def backspace():
    current_text = output_display.get("1.0", tk.END).strip()
    new_text = current_text[:-1]
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, new_text)

def disable_typing(event):
    return "break"

window = tk.Tk()
window.title("Kalkulator")

window.geometry("400x600")  # Menyesuaikan ukuran window lebih besar
window.config(bg="black")  # Latar belakang hitam

output_display = tk.Text(window, font=('Arial', 24, 'bold'), height=2, width=18, borderwidth=5, relief="sunken", bg="grey", fg="white")
output_display.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")
output_display.bind("<Key>", disable_typing)

buttons = [
    ('AC', 1, 0), ('%', 1, 1), ('±', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3)
]

for (text, row, column, *colspan) in buttons:
    button = tk.Button(window, text=text, font=('Arial', 18, 'bold'), bg="grey" if text.isdigit() or text == '.' else "orange", fg="white", bd=1)
    if text == 'AC':
        button.config(command=clear)
    elif text == '=':
        button.config(command=calculate)
    elif text == '±':
        button.config(command=lambda: click('-'))  # Membuat tombol ± menjadi tanda negatif
    elif text == '<':
        button.config(command=backspace)
    else:
        button.config(command=lambda t=text: click(t))
    
    button.grid(row=row, column=column, columnspan=colspan[0] if colspan else 1, sticky="nsew", padx=5, pady=5)

for i in range(6):
    window.grid_rowconfigure(i, weight=1)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()