print('Detailing calculator 1.0')

#Small car(2 doors / 4 door cars), medium car(SUVs / 4 doors), large car(trucks)

#Change these variables for inflation!
small_car = 50
medium_car = 70
large_car = 90
package_type = ['(1) Basic package -$10','(2) Intermediete package - $20','(3) Pro package - $25']
package_type_1 = 10
package_type_2 = 20
package_type_3 = 25

cust_name = input(str('What is the customer name?\n'))
cust_email = input(str('What is the customer email?\n'))

x = input(str('What kind of vehicle will you be detailing?\n1 - Small   2 - Medium  3 - Large\n'))

#Small car.
mes_small = f'Total cost: ${small_car}.'

#Medium car
mes_med = f'Total cost: ${medium_car}.'

#Large car
mes_large = f'Total cost: ${large_car}.'

#Control flow
if x == '1':    #Small
    addons = input(str('Additional charges? Y/N\n'))
    if addons == 'y':
        package_type = input(str('   (1) Basic package - $10\n   (2) Intermediete package - $20\n   (3) Pro package - $25\n'))
        if package_type == '1':
            price = int(small_car + package_type_1)
            print(f'Total cost: ${small_car + package_type_1}')
        elif package_type == '2':
            price = int(small_car + package_type_2)
            print(f'Total cost: ${small_car + package_type_2}')
        else:
            price = int(small_car + package_type_3)
            print(f'Total cost: ${small_car + package_type_3}')
    else:
        price = small_car
        print(mes_small)
elif x == '2':  #Medium
    addons = input(str('Additional charges? Y/N\n'))
    if addons == 'y':
        package_type = input(str('   (1) Basic package - $10\n   (2) Intermediete package - $20\n   (3) - Pro package - $25\n'))
        if package_type == '1':
            price = int(medium_car + package_type_1)
            print(f'Total cost: ${medium_car + package_type_1}')
        elif package_type == '2':
            price = int(medium_car + package_type_2)
            print(f'Total cost: ${medium_car + package_type_2}')
        elif package_type == '3':
            price = int(medium_car + package_type_3)
            print(f'Total cost: ${medium_car + package_type_3}')
    else:
        price = medium_car
        print(mes_med)
elif x == '3':  #Large
    addons = input(str('Additional charges? Y/N\n'))
    if addons == 'y':
        package_type = input(str('   (1) Basic package - $10\n   (2) Intermediete package - $20\n   (3) - Pro package - $25\n'))
        if package_type == '1':
            price = int(large_car + package_type_1)
            print(f'Total cost: ${large_car + package_type_1}')
        elif package_type == '2':
            price = int(large_car + package_type_2)
            print(f'Total cost: ${large_car + package_type_2}')
        elif package_type == '3':
            price = int(large_car + package_type_3)
            print(f'Total cost: ${large_car + package_type_3}')
    else:
        price = int(large_car)
        print(mes_large)
else:
    print('Error!')


#Write a reciept.
f = open('reciept.txt','w+')
if f.mode == 'w+':
    f.write(f'Customer name: {cust_name}\n')
    f.write(f'Customer email: {cust_email}\n')
    f.write(f'Vehicle type: {x}\n')
    f.write(f'Package type: {package_type}\n')
    f.write(f'Total cost: ${price}\n')
    f.write(f'Package types include:\n(1) Basic package - $10, (2) Intermediete package - $20, (3) Pro package - $25.\n')
    f.write('Thank you for choosing Straight 6 Performance!')
    f.close()
else:
    f.close()