# Get user to enter the price of the meals and also their numbers below 
# both adult's and child's meal are to be floating point
# the number of adults and children are to be in integers
child_meal = float(input('Please enter the price of a child meal:'))
adult_meal = float(input('Please enter the price of a adult meal: '))
num_of_children = int(input('please enter the number of children: '))
num_of_adults = int(input('please enter the number of adult: '))

#meal's subtotal is to be derived for each one. please note this is not the total amount.
subtotal_of_meal = (child_meal * num_of_children) + (adult_meal * num_of_adults)
print('subtotal: $', f'{subtotal_of_meal: .2f}')

#ask the user for the sales tax rate as a percentage. please note, ensure the numbers are not converted to something like 0.006 or 0.007 that is it should not be divided by 100
sales_tax_rate= float(input('please enter the sales tax rate: '))
sales_tax = float(subtotal_of_meal * sales_tax_rate/100)
print("Sales tax: $", f'{sales_tax: .2f}')

#add the subtotal of the meal and the sales tax to get the total price the customer will be paying 
total_price = (subtotal_of_meal + sales_tax)
print("Total price: $", f'{total_price: .2f}')

# to know the change, the user will need to enter the amount paid in 
amount_paid = float(input('please enter the amount paid:'))
change = (amount_paid - total_price)
print ('Change: $', f'{change: .2f}')