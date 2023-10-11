def hanoi(disks, start, end, filler):
    if disks != 1:
        hanoi(disks-1, start, filler, end)  #ย้ายแผ่นเล็กไปfillerก่อนเพื่อย้ายแผ่นใหญ่
        print(f'move {disks} from {start} to {end}')  #ย้ายแผ่นใหญ่ไปแท่นend
        hanoi(disks-1, filler, end, start)  #ย้ายแผ่นเล็กกลับไปend
    else:
        print(f'move {disks} from {start} to {end}')
disks = int(input("Enter disks : "))
hanoi(disks, 'A', 'C', 'B')