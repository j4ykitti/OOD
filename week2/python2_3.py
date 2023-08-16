class TorKham:
    def init(self):
        self.history = []

    def check_play(self,inp):
        com_history = inp
        curr = ''
        last = ''
        for i in range(len(com_history)):
            com = com_history[i].split(' ')[0]
            if com == 'R':
                self.history.clear()
                print('game restarted')
                curr = ''
                last = ''
                continue
            elif com == 'X':
                return
            word = com_history[i].split(' ')[1]
            curr = word
            if com == 'P':
                if self.check_word(last,curr) or last =='':
                    self.history.append(word)
                    last = curr
                    print(f"{word}' -> {self.history}")
                else: 
                    print(f"{word}' -> game over")


            else:
                print(f"{com} {word} 'is Invalid Input !!!'")
                return

    def check_word(self,last_word,new_word):
        last = last_word.lower()
        new = new_word.lower()
        #print(last[-2:],new[:2])
        if last[-2:] == new[:2]:
            return True
        return False
print(' TorKham HanSaa ')
game = TorKham()
inp = input('Enter Input : ').split(',')
game.check_play(inp)