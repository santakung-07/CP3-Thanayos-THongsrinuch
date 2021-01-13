# Exercise21 BMI measurement with tkinter GUI 
from tkinter import *

def BMI_measure(event):
    w = float(weightEntry.get())
    h = float(heightEntry.get())
    status = ""
    try:
        result = w/((h/100)**2)
        if result >=30:
            status = "อ้วนมาก"
        elif result >= 25:
            status = "อ้วน"
        elif result >= 23:
            status = "น้ำหนักตัวเกิน"
        elif result >= 18.5:
            status = "น้ำหนักปกติ"
        elif result < 0:
            status = "ใส่ค่าไม่ถูกต้อง"
        elif result < 18.5:
            status = "ผอมเกินไป"
        result = result.__format__(".2f")       # แก้ format เลขให้อ่านง่าย
        interpreted.config(text = "%s %s "%(result,status))     # แสดงทั้งค่า BMI และการแปลผล
    except Exception:
        interpreted.config(text = "ใส่ค่าไม่ถูกต้อง")        # ถ้า error ให้เข้า block นี้
    
window = Tk()
window.title("BMI Measurement")
window.option_add("*font","tahoma 10")

weightLabel = Label(window,text="weight(kg.)").grid(row=0,column=0,padx=5,pady=5)
weightEntry = Entry(window)
weightEntry.grid(row=0,column=1,padx=5,pady=5)

heightLabel = Label(window,text="height(cm.)").grid(row=1,column=0,padx=5,pady=5)
heightEntry = Entry(window)
heightEntry.grid(row=1,column=1,padx=5,pady=5)

calculated = Button(window,text="calculated")
calculated.bind('<Button-1>',BMI_measure)
window.bind('<Return>',BMI_measure)     # เพิ่มให้ กด enter ก็เข้า function ด้วย
calculated.grid(row=2,column=0,padx=5,pady=5)
interpreted = Label(window, text="result")
interpreted.grid(row=2, column=1,padx=5,pady=5)

window.mainloop()