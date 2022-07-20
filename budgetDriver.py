from budget import*

b=Budget()
b.greeting()
x=-1                                                                           #wrong input
while not 10000>x>0:                                                           #Error checking.Ensures the cost isn't outside the range
    try:
        c=input('How much is your expendable income? ')
        x=int(c.strip('$'))
        if not 100000>x>0:
            print('Your income must be non-negative and cannot exceed 5-digits')
    except ValueError:
            print('Your income must be a rational number')
b.setBudget(x)

print('You are to input an item name ,cost and quantity')
b.getItems()
b.CostList()
b.Total()

while b.itemChecker()==True:
    if b.suggestions()==True:
        pass
    else:
        b.itemChecker()
else:
    b.getPercentage()
    b.displayTable()
