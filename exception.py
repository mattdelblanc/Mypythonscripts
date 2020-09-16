print ('How many cats do you have?')
num_cats = input ()

try:
    if int(num_cats) >= 4:
        print('You are totally a cat person')
    elif int(num_cats) < 0:
        print('You did not type a real number')
    else :
        print('You are meh')
except ValueError:
    print('You did not add a number')          