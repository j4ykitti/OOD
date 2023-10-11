def compare_power(l1, l2, count):
    if sum_team(l1) > sum_team(l2):
        sign = '>'
    elif sum_team(l1) < sum_team(l2):
        sign = '<'
    elif sum_team(l1) == sum_team(l2):
        sign = '='

    print(f'{l1}{sign}{l2}')
    if count+2 > len(teamComp):
        return  
    return compare_power(teamComp[count], teamComp[count+1], count+2)
    
def sum_team(l):
    if l > len(power)-1:
        return 0
    return power[l] + sum_team(l*2+1) + sum_team(l*2+2)

inp = input('Enter Input : ').split('/')
teamComp = []
power = []
inp[0] = inp[0].split(' ')
inp[1] = inp[1].split(',')
for i in inp[0]:
    power.append(int(i))
for i in inp[1]:
    temp = i.split(' ')
    teamComp.append(int(temp[0]))
    teamComp.append(int(temp[1]))
print(sum(power))
compare_power(teamComp[0], teamComp[1], 2)