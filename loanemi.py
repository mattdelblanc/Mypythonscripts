def loan (amount,duration):
    emi = amount/duration
    return emi

emi_1 = loan(1260000,8*12)
print(emi_1)
emi_2 = loan(1260000,10*12)
print(emi_2)    

difference = emi_1 -emi_2
print(difference)
