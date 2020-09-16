first = input()
second = input()
third = input()

if first >= second and first >= third:
    print('first is oldest')
elif second >= first and second >=third:
    print('second is oldest')
elif third >= first and third >= second:
    print('third is oldest')

else:
    print('all are equal')    