import tkinter as tk
from tkinter import messagebox, ttk

def turing_machine(input_string):
    tape = list(input_string) + ['B']
    state = 'q9'
    head = 0
    while state != 'q0' and state != "qr":
        if state == 'q9':
            if tape[head] == '1':
                state = 'q10'
                head += 1
            else:
                state = 'qr'
        elif state == 'q10':
            if tape[head] == '0':
                state = 'q11'
                head += 1
            else:
                state = 'qr'
        elif state == 'q11':
            if tape[head] == '+':
                state = 'q0'
                head += 1
            else:
                state = 'qr'

    if head + 1 >= len(tape):
        return state == 'qr'
    else:
        tape = tape[0:head] + ['0'] + tape[head + 1:]
        if len(tape) > 2:
            tape[2] = '1'
        head = 0

    while state != 'q8' and state != 'qr':
        if state == 'q0':
            if tape[head] == '1' or tape[head] == '0':
                state = 'q1'
                head += 1
            elif tape[head] == 'B':
                state = 'qr'
            else:
                state = 'qr'

        elif state == 'q1':
            if tape[head] == '0' or tape[head] == '1':
                state = 'q1'
                head += 1
            elif tape[head] == 'B':
                state = 'q2'
                head -= 1
            else:
                state = 'qr'

        elif state == 'q2':
            if tape[head] == '1':
                state = 'q2'
                head -= 1
            elif tape[head] == '0':
                state = 'q3'
                tape[head] = '1'
                head += 1
            else:
                state = 'qr'

        elif state == 'q3':
            if tape[head] == '1':
                state = 'q4'
                tape[head] = '0'
                head += 1
            else:
                state = 'qr'

        elif state == 'q4':
            if tape[head] == '0' or tape[head] == 'B':
                state = 'q4'
                head -= 1
            elif tape[head] == '1':
                state = 'q5'
                head -= 1
            else:
                state = 'qr'

        elif state == 'q5':
            if tape[head] == '1':
                state = 'q5'
                head -= 1
            elif tape[head] == '0':
                state = 'q3'
                tape[head] = '1'
                head += 1
            elif tape[head] == 'B':
                state = 'q6'
                head += 1
            else:
                state = 'qr'
        elif state == 'q6':
            if tape[head] == '1':
                state = 'q6'
                head += 1
            elif tape[head] == '0':
                state = 'q7'
                tape[head] = 'B'
                head += 1
            else:
                state = 'qr'
        elif state == 'q7':
            if tape[head] == '0':
                state = 'q7'
                tape[head] = 'B'
                head += 1
            elif tape[head] == 'B':
                state = 'q8'
                head -= 1
            else:
                state = 'qr'

    string_result = list(tape)
    for i in range(len(string_result)):
        if string_result[i] == 'B':
            string_result[i] = ''

    return state == 'q8', ''.join(string_result)

def validate_string():
    input_string = entry.get()
    resultado = turing_machine(input_string)

    if resultado[0]: 
        messagebox.showinfo("Resultado", "¡Cadena válida!")
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, resultado[1])
        result_entry.config(state='readonly')
    else:
        messagebox.showwarning("Resultado", "Cadena inválida.")
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.config(state='readonly')

root = tk.Tk()
root.title("Máquina de Turing - Suma de Decimal con Binario")
root.geometry("700x250")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(expand=True)

input_label = ttk.Label(main_frame, text="Ingresa la cadena (formato '10+[Cadena Binaria]'):", font=("Arial", 12))
input_label.grid(row=0, column=0, columnspan=2, pady=5)

entry = ttk.Entry(main_frame, width=40, font=("Arial", 10))
entry.grid(row=1, column=0, padx=10, pady=5)

validate_button = ttk.Button(main_frame, text="Validar Cadena", command=validate_string)
validate_button.grid(row=1, column=1, padx=10, pady=5)

result_label = ttk.Label(main_frame, text="Cadena resultante:", font=("Arial", 12))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

result_entry = ttk.Entry(main_frame, width=50, font=("Arial", 10), state='readonly')
result_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
