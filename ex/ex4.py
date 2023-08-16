# รับข้อความ 2 ข้อความ

# ข้อความแรกให้หมุนขวาสองตำแหน่ง ข้อความที่สองให้หมุนซ้ายสามตำแหน่ง

# แสดงผลแต่ละครั้งของการหมุน

# หยุดเมื่อข้อความที่หมุน เหมือนข้อความที่รับเข้ามา

# โดยแสดงผล 5 บรรทัดแรก และบรรทัดสุดท้าย
# Enter 2 strings : 1234567 abcabcabc
# 1 6712345 abcabcabc
# 2 4567123 abcabcabc
# 3 2345671 abcabcabc
# 4 7123456 abcabcabc
# 5 5671234 abcabcabc
#  . . . . . 
# 7 1234567 abcabcabc
# Total of  7 rounds.
print("*** String Rotation ***")
message = str(input("Enter 2 strings : "))
mes = message.split()
ls1 = str(mes[0])
rs1 = str(mes[0])
ls2 = str(mes[1])
rs2 = str(mes[1])
x = 0
while x < 5:
    
    First1 = ls1[-2:]
    Second1 = ls1[:-2]
    First2 = ls2[3:]
    Second2 = ls2[:3]
    ls1 = First1+Second1
    ls2 = First2+Second2
    x = x+1
    print(f"{x}"+" "+f"{ls1}"+" "+f"{ls2}")
    if ls1 == rs1 and ls2 == rs2:
        print(f"Total of  {x} rounds.")
        break

print(" . . . . . ")
while ls1 != rs1 or ls2 != rs2:
    First1 = ls1[-2:]
    Second1 = ls1[:-2]
    First2 = ls2[3:]
    Second2 = ls2[:3]
    ls1 = First1+Second1
    ls2 = First2+Second2
    x = x+1
print(f"{x} Wonderful Saphetti")
print(f"Total of  {x} rounds.")







