"""
lecture 73 
    โปรแกรมแสดงบิล แก้ไขให้ดีขึ้น
    กรอก menu เรื่อยๆจนกรอก exit
    แสดงราคารวมสินค้า แบบ collection ซ้อน collection
    เก็บราคาไว้แล้วใน dict
"""
systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []
totals = 0
def showBill():
    print("---My food---")
    for x in range(len(menuList)):  
        print(menuList[x][0], "=", menuList[x][1])
    global totals
    for i in range(len(menuList)):
        totals += menuList[i][1]
    print("totals =", totals)
while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":  
        showBill()
        break
    elif menuName not in systemMenu.keys():     # เผื่อพิมพ์เมนูนอก key ให้ข้ามไปเลย
        continue
    else:
        menuList.append([menuName, systemMenu[menuName]])  # รวมแต่ละครั้งการกรอกไว้ใน list ย่อยเดียวกัน