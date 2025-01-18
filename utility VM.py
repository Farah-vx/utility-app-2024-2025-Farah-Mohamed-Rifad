#available products in the vending machine
products = {
    'Crisps': {
        'A1': ('lays', 2.50),
        'A2': ('doritos',3.00),
        'A3': ('takis', 4.00),
        'A4': ('cheetos',2.50),
        'A5': ('chips oman', 1.00)},
    
    'Biscuits': {
        'B1': ('Hello panda', 2.50),
        'B2': ('biscoff', 3.00),
        'B3': ('oreo', 2.50),
        'B4': ('Chunko', 2.00),
        'B5': ('Loacker', 4.00)},

    'Chocolates': {
        'C1': ('milka', 4.00),
        'C2': ('Twix', 4.00),
        'C3': ('m&m', 3.50),
        'C4': ('Hersheys', 4.00),
        'C5': ('galaxy', 3.00)},
    
    'Carbonated beverages': {
        'D1': ('cola', 3.00),
        'D2': ('7up', 3.00),
        'D3': ('Dew', 3.00),
        'D4': ('Diet Pepsi', 3.00),
        'D5': ('fanta', 3.00)},
    
    'Non-Carbonated Beverages': {
        'E1': ('water', 1.50),
        'E2': ('Lipton lemon', 4.00),
        'E3': ('Lipton peach', 4.00),
        'E4': ('Nescafe original', 5.00),
        'E5': ('Nescafe Macha', 4.50)}}

#welcoming the user
print('\n HELLO!, READY TO GRAB A TREAT?')
    
    
#displaying an organised output of each item that are available in the vending machine with its price
def display():

    print('\nAvailable items: ')
    print('----------------------------------------------------------------')
    print(f' {"code":<6} {"category":<25} {"item":<20} {"cost":<10}')
    print('----------------------------------------------------------------')
    for category, items in products.items():
         for product_code, (product_name, product_cost) in items.items():
           
             print(f'{product_code:<6} {category:<25} {product_name:<20} ${product_cost:<9.2f}')

    print('----------------------------------------------------------------')
display()

def blank():
    print('----------------------------')
#asking the user to input the product code of their choice
def query():
    user = input('\nEnter your desired product number: ').strip().upper()
    return user

 # creating a Loop until the user selects a valid product code and outputting the price and name of the product chosen
def select_item():
    cart=[] 
    sum_cost = 0
    while True:
        user = query()
        for category, items in products.items():
            if user in items:
                product_name, product_cost = items[user]
                print(f"\nYou have selected {user} - {product_name} = ${product_cost:.2f}")
                sum_cost += product_cost
                cart.append(product_name)
                return sum_cost, cart
        print('Invalid code, please try again.')

#asking if they would want to add something more or not 
def new_query():
    while True: 
        user = input('\nwould you like somthing more?)(click: 1 if yes or 2 for no):').strip().lower()
        if user == '1':
            return True
        elif user == '2':
            return False
        print('invalid code, please try again')
    

#proceding to payment & outputting the total cost of the total items chosen by the user
def cash(sum_cost,cart):
        while True:
            try:
                print(f'\nTotal cost is ${sum_cost:.2f}')
                user = float(input('\nInsert your cash: '))  
                if user >= sum_cost: 
                   balance = user - sum_cost
                   print(f'\nTotal cost is ${sum_cost:.2f}, cash inputted ${user:.2f},balance amount ${balance:.2f}')#showing their balance amount for the cash they had inputted
                   print(f'\n{cart} has been successfully dispensed :')#dispencing the items after checkout
                   print('\n     WE APPRECIATE YOUR PURCHASE!')
                   print('\n')
                   break
                elif user < sum_cost:
                  balance = sum_cost - user
                  print(f'insufficient input amount ${user}, please input the correct amount')
            except:
                print('value error')

sum_cost = 0
cart = []  
while True:
    cost, items = select_item() #creating an infinite loop to keep requesting user for items
    sum_cost += cost #adding total cost of all chosen item
    cart.extend(items) #adding the items to cart
    if not new_query(): #asking user if they want to continue or end
        break

#calling cash function
cash(sum_cost, cart)
