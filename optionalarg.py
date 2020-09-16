def loan_emi(amount, duration,down_payment= 0):
    loan_amount = amount - down_payment
    emi = amount/duration
    return emi

emi_1 = loan_emi(1260000,8*12,300000)
print(emi_1)
emi_2 = loan_emi(1260000,10*12)
print(emi_2)

difference = emi_1-emi_2
print(difference)

