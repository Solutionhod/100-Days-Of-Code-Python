from tkinter import *


def miles_to_kilometer():
    miles = float(mile_input.get())
    km = round((miles * 1.609), 2)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.minsize(width=500, height=500)
window.title("Miles To Kilometer Converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_to_label = Label(text="Is equal to")
is_equal_to_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)

window.mainloop()