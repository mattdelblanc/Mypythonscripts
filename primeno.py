num = input()

if num > 1:
    for i in range (2,num):
        if num%i == 0:
            print('not a prime number')
            break
    else:
        print('Prime number')

else:
    print('Not a prime number')
