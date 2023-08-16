class MyInt:
    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    rom = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    def init(self, inte):
        self.inte = inte

    def toRoman(self):
        str = ''
        temp = self.inte
        div = 1
        i = 12 
        while temp:
            div = temp // self.num[i]
            temp %= self.num[i]

            while div:
                str += self.rom[i]
                div -= 1
            i -= 1
        return str

    def add(self,myint2):
        return ((self.inte + myint2.inte)3)//2

print(' *** class MyInt ***')
nums = input('Enter 2 number : ').split(' ')
num1 = MyInt(int(nums[0]))
num2 = MyInt(int(nums[1]))
print(str(num1.inte) + ' convert to Roman : ' + num1.toRoman())
print(str(num2.inte) + ' convert to Roman : ' + num2.toRoman())
sum = num1 + num2
print(str(num1.inte) + ' + ' + str(num2.inte) + ' = ' + str(sum))
