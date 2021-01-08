# exercise 11 สร้าง pyramid *
print("---star pyramid---")
numberOfLevels = int(input("insert number of levels"))
blankSpace = numberOfLevels
print("input ",blankSpace*" "," output")
print(numberOfLevels,end="")
for i in range (numberOfLevels):
    blankSpace -= 1
    print(3*"\t"," "*blankSpace,"*"*((i*2)+1))
# เว้นระยะ 3 tabs ก่อนใน pycharm แสดงผลปกติดีแต่ใน vscode ตำแหน่งจะไม่เป๊ะ
