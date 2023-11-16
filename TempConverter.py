import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

#creating a home window:

root = tk.Tk()
root.title('Temperature Converter')
root.geometry('540x240')
root.resizable(False, False)

# function to convert fahrenheit to celsius:

def fahrenheit_to_celsius(f):
    """ Convert fahrenheit to celsius
    """
    return (f - 32) * 5/9

# function to convert celsius to fahrenheit:

def celsius_to_fahrenheit(c):
    """convert celsius to fahrenheit
    """
    return (c * 9/5) + 32


# Crreating a frame

frame = ttk.Frame(root)


# adjusting the field options

options = {'padx': 5, 'pady': 5}

# to create a temperature label to store fahrenheit value

temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# to create a temp label to store celsius value

temp_label = ttk.Label(frame, text='Celsius')
temp_label.grid(column=0, row=3, sticky='W', **options)

# temperature in fahrenheit entry
temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

#temp in celsius entry
temp = tk.StringVar()
temp_entry = ttk.Entry(frame, textvariable=temp)
temp_entry.grid(column=1, row=3, **options)
temp_entry.focus()

# convert button for Fahrenheit Conversion:

def convert_button_clicked():
    """  Handle convert button click event 
    """
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius(f)
        result = f'{f} Fahrenheit = {c:.2f} Celsius'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)

# convert button for Celsius Conversion:

def convert_clicked():
    """  Handle convert button click event 
    """
    try:
        c = float(temp.get())
        f = celsius_to_fahrenheit(c)
        res = f'{c:.2f} Celsius = {f} Fahrenheit'
        res_label.config(text=res)
    except ValueError as error:
        showerror(title='Error', message=error)


convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

convt_button = ttk.Button(frame, text='Convert')
convt_button.grid(column=2, row=3, sticky='W', **options)
convt_button.configure(command=convert_clicked)

# result label for fahrenheit conversion
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# res label for celsius conversion

res_label = ttk.Label(frame)
res_label.grid(row=4, columnspan=3, **options)

# adding padding to the frame:
frame.grid(padx=10, pady=10)


# calling the mainloop to run the app
root.mainloop()