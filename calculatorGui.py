from customtkinter import *
import re

"Function to compute and display the result"
def calc():
    try:
        values = value_display.get()
        values = values.replace('x', '*').replace('÷', '/').replace('mod', '%')
        list_of_values = re.split(r'([+\-*/%()])', values)
        result = eval(''.join(list_of_values))
        answer_display.delete(0, len(answer_display.get()))
        answer_display.insert(END, result)
    except SyntaxError:
        answer_display.delete(0, len(answer_display.get()))
        answer_display.insert(END, "ERROR")

"Function to get the answer from the answer_display and display it on the value_display"
def ans():
    value_display.delete(0, len(value_display.get()))
    value_display.insert(END, answer_display.get())

"Function to display character in the value_display"
def display_item(a):
    value_display.insert(value_display.index(INSERT), a)

"Function to delete everything in the value_display and answer_display"
def clear():
    value_display.delete(0, len(value_display.get()))
    answer_display.delete(0, len(answer_display.get()))

"Function to delete a single character in the value_display"
def delete():
    value_display.delete((value_display.index(INSERT) - 1), value_display.index(INSERT))


window = CTk()
window.title("CALCULATOR")
window.minsize(width=375, height=450)
window.maxsize(width=375, height=450)

# Entry
value_display = CTkEntry(master=window, width=375, height=75, font=("Comic Sans", 30))
value_display.grid(row=0, column=0, columnspan=5)
value_display.focus()

answer_display = CTkEntry(master=window, width=150, height=75, font=("Comic Sans", 30))
answer_display.grid(row=1, column=3, columnspan=2)
answer_display.focus()

# Buttons
zero_button = CTkButton(master=window, text="0", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(0))
zero_button.grid(row=5, column=0)

one_button = CTkButton(master=window, text="1", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(1))
one_button.grid(row=4, column=0)

two_button = CTkButton(master=window, text="2", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(2))
two_button.grid(row=4, column=1)

three_button = CTkButton(master=window, text="3", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(3))
three_button.grid(row=4, column=2)

four_button = CTkButton(master=window, text="4", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(4))
four_button.grid(row=3, column=0)

five_button = CTkButton(master=window, text="5", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(5))
five_button.grid(row=3, column=1)

six_button = CTkButton(master=window, text="6", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(6))
six_button.grid(row=3, column=2)

seven_button = CTkButton(master=window, text="7", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(7))
seven_button.grid(row=2, column=0)

eight_button = CTkButton(master=window, text="8", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(8))
eight_button.grid(row=2, column=1)

nine_button = CTkButton(master=window, text="9", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(9))
nine_button.grid(row=2, column=2)

add_button = CTkButton(master=window, text="+", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item("+"))
add_button.grid(row=2, column=3)

subtract_button = CTkButton(master=window, text="-", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item("-"))
subtract_button.grid(row=3, column=3)

multiply_button = CTkButton(master=window, text="x", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item("x"))
multiply_button.grid(row=4, column=3)

divide_button = CTkButton(master=window, text="÷", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item("÷"))
divide_button.grid(row=5, column=3)

delete_button = CTkButton(master=window, text="DEL", width=75, height=75, font=("Comic Sans", 30), command=delete)
delete_button.grid(row=2, column=4)

clear_button = CTkButton(master=window, text="C", width=75, height=75, font=("Comic Sans", 30), command=clear)
clear_button.grid(row=3, column=4)

equal_button = CTkButton(master=window, text="=", width=75, height=150, font=("Comic Sans", 30), command=calc)
equal_button.grid(row=4, column=4, rowspan=2)

answer_button = CTkButton(master=window, text="Ans", width=75, height=75, font=("Comic Sans", 30), command=ans)
answer_button.grid(row=5, column=2)

point_button = CTkButton(master=window, text=".", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item("."))
point_button.grid(row=5, column=1)

left_bracket_button = CTkButton(master=window, text="(", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item("("))
left_bracket_button.grid(row=1, column=0)

right_bracket_button = CTkButton(master=window, text=")", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item(")"))
right_bracket_button.grid(row=1, column=1)

modulus_button = CTkButton(master=window, text="mod", width=75, height=75, font=("Comic Sans", 30), command=lambda: display_item("mod"))
modulus_button.grid(row=1, column=2)

window.mainloop()
