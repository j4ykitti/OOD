class Hash:
    def __init__(self, table_size, max_collision, threshold):
        self.table_size = table_size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * table_size

    def isFull(self):
        cur, des = 0, int(self.table_size * self.threshold / 100)
        for i in self.table:
            if i is not None:
                cur += 1
        if cur >= des:
            return True
        return False
    
    def insert(self, value):
        if not self.isFull():
            idx = value % self.table_size

            if self.table[idx] is None:
                self.table[idx] = value

            elif self.table[idx] is not None:
                collision = 0
                print(f'collision number {collision + 1} at {idx}')

                while self.table[idx] is not None:
                    collision += 1
                    new_idx = (idx + collision * collision) % self.table_size

                    if collision >= self.max_collision:
                        print("****** Max collision - Rehash !!! ******")
                        return False
                    
                    if self.table[new_idx] is None:
                        self.table[new_idx] = value
                        break

                    print(f'collision number {collision + 1} at {new_idx}')
            return True
        else:
            print('****** Data over threshold - Rehash !!! ******')
            return False

    def print_table(self):
        for i in range(len(self.table)):
            print(f'#{i+1}'+ " " * (7-len(str(i+1))) + f'{self.table[i]}')

def find_next_prime(value):
    while value:
        value += 1
        for i in range(2, value):
            if value % i == 0:
                break
            if i == value - 1:
                return value

print(' ***** Rehashing *****')
inp = input('Enter Input : ').split('/')
table_size, max_collision, threshold = map(int, inp[0].split())
data_list = list(map(int, inp[1].split()))
hash = Hash(table_size, max_collision, threshold)

print('Initial Table :')
hash.print_table()
print('----------------------------------------')

lastAdd, notAll = -1, True
while notAll:
    for i in range(len(data_list)):
        if i >= lastAdd + 1:
            print(f'Add : {data_list[i]}')
        if not hash.insert(data_list[i]):
            hash = Hash(find_next_prime(hash.table_size * 2), max_collision, threshold)
            lastAdd = i
            break
        else:
            if i >= lastAdd:
                hash.print_table()
                print('----------------------------------------')
        if i == len(data_list) - 1:
            notAll = False