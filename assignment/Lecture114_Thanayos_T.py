# โปรเจ็ค  Lecture 114 
"""
    สร้าง GUI , convert ค่าเงิน , วาดกราฟ สัปดาห์ เดือน ปี
"""
import matplotlib.pyplot as plt
from datetime import datetime
from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates

# กำหนด list of currency

c = CurrencyRates()
rate = c.get_rates('USD')   
list_currency = []
for currency in rate:     # loop เพื่อดึงเฉพาะ สกุลเงินซึ่งเป็น key ใส่ใน list
    list_currency.append(currency)

# สร้าง GUI

window = Tk()
window.title("Currency converter")

# function แปลงสกุลเงิน

def currency_converter(*arg):
    result = c.convert(combo_box_from.get(), combo_box_to.get(), entry_from_var.get())
    entry_to_var.set(result.__format__(".2f"))
  
# Winget ใส่สกุลเงิน

text_from = Label(window, text = "from").grid(row = 1, column = 0, padx = 10, pady = 10)
entry_from_var = DoubleVar()
entry_from_var.trace_add("write",currency_converter)        # เชื่อมการแก้ DoubleVar()
entry_from = Entry(window, textvariable = str(entry_from_var))
entry_from.grid(row = 1, column = 1, padx = 10, pady = 10)
combo_box_from = ttk.Combobox(window, value = list_currency, width = 5)
combo_box_from.current(0)
combo_box_from.bind("<<ComboboxSelected>>",currency_converter)
combo_box_from.grid(row = 1, column = 2, padx = 10, pady = 10)

text_to =  Label(window, text = "to").grid(row = 2, column = 0)
entry_to_var = DoubleVar()
entry_to_var.trace_add("write",currency_converter)      # เชื่อมการแก้ DoubleVar()
entry_to = Entry(window, state = DISABLED, textvariable = str(entry_to_var))
entry_to.grid(row = 2, column = 1)
combo_box_to = ttk.Combobox(window, value = list_currency, width = 5)
combo_box_to.current(0)
combo_box_to.bind("<<ComboboxSelected>>",currency_converter)
combo_box_to.grid(row = 2, column = 2)


# winget ปุ่มค่าเฉลี่ย

graph_frame = LabelFrame(text = "graph") 
graph_frame.grid(row = 3 ,column = 0, columnspan = 2, padx = 10, pady = 10)
button_week = Button(graph_frame, text = "Week")
button_week.pack(side = LEFT, padx = 10, pady = 10)
button_month = Button(graph_frame, text = "Month")
button_month.pack(side = LEFT,padx = 10, pady = 10)
button_year = Button(graph_frame, text = "Year")
button_year.pack(side = LEFT,padx = 10, pady = 10)

# วาดกราฟ



mainloop()