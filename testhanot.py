def hanoi(disk, start, end, filler):
    if disk != 1:
        hanoi(disk-1,start,filler,end)
        print(f'move {disk} from {start} to {end}')
        hanoi(disk-1,filler,end,start)
    else:
        print(f'move{disk} from {start} tp {end}')

hanoi(3,'a','c','b')