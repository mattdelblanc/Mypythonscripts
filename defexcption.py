def number(number_2):
    try:
        return 20/number_2
    except ZeroDivisionError:
        print('you tried to divide by 0')   

print (number(20))
print (number(100))
print (number(0))