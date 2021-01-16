# โปรเจ็ค  Lecture 114 สร้าง GUI , convert ค่าเงิน , วาดกราฟ สัปดาห์ เดือน ปี

import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates

# กำหนด list of currency 

c = CurrencyRates()
rate = c.get_rates('USD')   
list_currency = []
for currency in rate:     # loop เพื่อดึงเฉพาะ สกุลเงินซึ่งเป็น key ใส่ใน list
    list_currency.append(currency)

# function แปลงสกุลเงิน

def currency_converter(*arg):
    result = c.convert(combo_box_from.get(), combo_box_to.get(), entry_from_var.get())
    entry_to_var.set(result.__format__(".2f"))


# function วาดกราฟ

def button_click(button):
    t = button.cget("text")     # t คือ ตัวแปรสำหรับรับ text ของปุ่ม
    today = datetime.now()
    list_date = [today.date()]      # แกน x เก็บ list ของ date
    list_rate = [c.get_rate(combo_box_from.get(), combo_box_to.get(), today)]   # แกน  y กับ list ของ exchange rate
    if t == "Lasted 7 days":        # ให้ mark จุด 7 นับจากวันนี้ ถอยไป 7 วัน
        for i in range(6):
            date_range = timedelta(days = -1)       # date_range แทนขนาดช่วง timedelta
            date_minus = today.__add__(date_range)      # date_minus แทนวันที่ลบ timedelta ไปแล้ว
            list_date.append(date_minus.date())
            list_rate.append(c.get_rate(combo_box_from.get(), combo_box_to.get(), date_minus.date()))
            today = date_minus       
    if t == "Lasted 30 days":
        for i in range(6):      # ให้ mark จุด 7 นับจากวันนี้ ถอยไป 30 วัน
            date_range = timedelta(days = -5)
            date_minus = today.__add__(date_range)
            list_date.append(date_minus.date())
            list_rate.append(c.get_rate(combo_box_from.get(), combo_box_to.get(), date_minus.date()))
            today = date_minus     
    if t == "Lasted 12 months":
        for i in range(11):     # ให้ mark จุด 12 นับจากวันนี้ ถอยไปทุกเดือนจนครบ 12 เดือน
            date_range = timedelta(days = -30)
            date_minus = today.__add__(date_range)
            list_date.append(date_minus.date())
            list_rate.append(c.get_rate(combo_box_from.get(), combo_box_to.get(), date_minus.date()))
            today = date_minus
    rate_avg = (sum(list_rate)/len(list_rate)).__format__(".4f")        # เก็บค่าเฉลี่ย
    rate_max = (max(list_rate)).__format__(".4f")       # เก็บค่า max
    rate_min = (min(list_rate)).__format__(".4f")       # เก็บค่า min
    plt.style.use("seaborn")
    plt.title(f"avg = {rate_avg}, max = {rate_max}, min = {rate_min}")
    plt.suptitle(f"Exchange rate 1 {combo_box_from.get()} >> {combo_box_to.get()} {t}")
    plt.ylabel("exchange rate")
    plt.xlabel("date")
    plt.plot(list_date, list_rate, linestyle = ":", color = "red", marker = "s")
    plt.show()
  
# สร้าง GUI

window = Tk()
window.title("Currency converter")
window.option_add("*font","colidia 18")
window.config(bg = "#fff5cc")

# Winget ใส่สกุลเงิน

text_from = Label(window, text = "from", bg = "#fff5cc", fg = "red").grid(row = 1, column = 0, padx = 10, pady = 10)
entry_from_var = DoubleVar()
entry_from_var.trace_add("write",currency_converter)        # เชื่อมการแก้ DoubleVar()
entry_from = Entry(window, textvariable = str(entry_from_var))
entry_from.grid(row = 1, column = 1, padx = 10, pady = 10)
combo_box_from = ttk.Combobox(window, value = list_currency, width = 5)
combo_box_from.current(10)
combo_box_from.bind("<<ComboboxSelected>>",currency_converter)
combo_box_from.grid(row = 1, column = 2, padx = 10, pady = 10)

text_to =  Label(window, text = "to", bg = "#fff5cc", fg = "green").grid(row = 2, column = 0)
entry_to_var = DoubleVar()
entry_to_var.trace_add("write",currency_converter)      # เชื่อมการแก้ DoubleVar()
entry_to = Entry(window, state = DISABLED, disabledbackground = "#daece6", disabledforeground = "#183f49", textvariable = str(entry_to_var))
entry_to.grid(row = 2, column = 1)
combo_box_to = ttk.Combobox(window, value = list_currency, width = 5)
combo_box_to.current(29)
combo_box_to.bind("<<ComboboxSelected>>",currency_converter)
combo_box_to.grid(row = 2, column = 2)

# winget ปุ่มวาดกราฟ

graph_frame = LabelFrame(text = "graph and statistic data", bg = "#fff5cc") 
graph_frame.grid(row = 3 ,column = 0, columnspan = 3, padx = 10, pady = 10)
button_week = Button(graph_frame, text = "Lasted 7 days", command = lambda :button_click(button_week))
button_week.pack(side = LEFT, padx = 10, pady = 10)
button_month = Button(graph_frame, text = "Lasted 30 days", command = lambda :button_click(button_month))
button_month.pack(side = LEFT,padx = 10, pady = 10)
button_year = Button(graph_frame, text = "Lasted 12 months", command = lambda :button_click(button_year))
button_year.pack(side = LEFT,padx = 10, pady = 10)

mainloop()