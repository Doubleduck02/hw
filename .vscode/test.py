print(ascii('│'))
print(ascii('─'))
print(ascii('┼'))
print('\u2500'*3)
print(ascii('└'))
print(ascii('┴'))
print(ascii('┘'))
tab=[]
x=[' ']
x.append(' ')
x.append(' ')
for i in range(3):
    tab.append(x)
    if i in range(1,3):
        print(i)
print(tab)