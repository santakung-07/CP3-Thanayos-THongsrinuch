"""
lecture 72 
    โปรแกรมแสดงบิล
    กรอก menu และ ราคาเรื่อยๆจนกรอก exit
    แสดงราคารวมสินค้า แบบ coleection ซ้อน collection
"""
menuList = []
totals = 0
while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":      # ให้ check โดยแปลงเป็น lower ให้หมดถ้ากรอก exit ก็ออก loop เลย
        break
    else:
        menuPrize = int(input("Price: "))
        menuList.append([menuName,menuPrize])       # รวมแต่ละครั้งการกรอกไว้ใน list ย่อยเดียวกัน
def showBill():
    print("---My food---")
    for x in range(len(menuList)):      # ทำแบบนี้ได้เลยเพราะสมาชิก ทั้ง 2 list เท่ากันและกรอกมาคู่กัน
        print(menuList[x][0],"=",menuList[x][1])
    global totals
    for i in range(len(menuList)):
        totals += menuList[i][1]
    print("totals =",totals)
showBill()
