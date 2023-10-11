def hanoi(disk, start, end, filler):
    if disk != 1:
        hanoi(disk-1,start,filler,end)
        print(f'move {disk} from {start} to  {end}')
        hanoi(disk-1,filler,end,start)
    else:
        print(f'move {disk} from {start} to {end}')
        

disk = int(input("Enter disks : "))
hanoi(disk,'A','C','B')