#L4 Problem Set2-1
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
 
for i in range(12):
    mIR = annualInterestRate/12.0
    mMP = balance * monthlyPaymentRate
    mUB = balance - mMP
    Ub = mUB + mUB * mIR
    balance = Ub
print("Remaining balance:"+str(round(Ub,2)))




#L4 Problem Set2-2
balance = 4773
annualInterestRate = 0.2
mIR = annualInterestRate/12.0

def yearPay(monthPay,balance,mIR):
    '''
    input:monthPay,balance,monthInterestRate
    output:remain balance after a year
    '''
    for i in range(12):
        mUB = balance - monthPay
        Ub = mUB + mUB * mIR
        balance = Ub
    return balance
    
monthPay = 10
while yearPay(monthPay,balance,mIR) > 0:
    monthPay +=10
else:
    print("Lowest Payment: "+str(monthPay))




##L4 Problem Set2-3
balance = 320000
annualInterestRate = 0.2
mIR = annualInterestRate/12.0

def yearPay(monthPay,balance,mIR):
    '''
    input:monthPay,balance,monthInterestRate
    output:remain balance after a year
    '''
    for i in range(12):
        mUB = balance - monthPay
        Ub = mUB + mUB * mIR
        balance = Ub
    return balance

upper = (balance * (1 + mIR)**12) / 12.0
lower = balance / 12
monthPay = (upper+lower)/2

while True:
    temp = yearPay(monthPay,balance,mIR) 
    if temp > 0:
        lower = monthPay
        monthPay = (upper+lower)/2
    elif temp < 0:
        upper = monthPay
        monthPay = (upper+lower)/2
    if abs(temp) <= 0.001:
        break
print("Lowest Payment: "+str(round(monthPay,2)))