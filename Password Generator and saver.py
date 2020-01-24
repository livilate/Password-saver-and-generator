import random

ongoing = True
variables = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ!@#$%^&*()'
information = {
}

#MAIN LOOP

while ongoing:

    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Get a random password")
    print(" 3. Save a password")
    print(" 4. Quit program")
    information.clear()
    choice = int(input('select a Number: '))

    if choice == 1:
        psaved = open('Documents\Password\Psaved.txt', 'r')
        print (psaved.read())
        psaved.close()

        cont = input('do you want to continue using the app? Type 1 if you want to, type any other key to close: ')

        if cont == '1':
            ongoing = True
        else:
            print('Thanks for using the app!!!')
            ongoing = False
        
    if choice == 2:
        lpassword = int(input('how many characters do you want your password to have? '))
        password = "".join(random.sample(variables, lpassword))

        print('----------------------------')
        print ('your password is: ', password)
        print('----------------------------')
        answer = input('press 1 to save the password or any other key wil close the app: ')

        if answer == '1':
            account_name = input('Enter your account name: ')
            information[account_name] = password
            #Just to save the dict on the pkl file.
            psaved = open('Documents\Password\Psaved.txt', 'a')
            psaved.write('\n'+str(information))
            psaved.close()

            cont = input('do you want to continue using the app? Type 1 if you want to, type any other key to close:  ')

            if cont == '1':
                ongoing = True
            else:
                print('Thanks for using the app!!!')
                ongoing = False
            
        else:
            print('Thanks for using this app!!!!!')
            ongoing = False

    if choice == 3:
        account_name = input('Enter your account name: ')
        password = input('Enter your password: ')
        information[account_name] = password
        psaved = open('Documents\Password\Psaved.txt', 'a')
        psaved.write('\n'+str(information))
        psaved.close()

        cont = input('do you want to continue using the app? Type 1 if you want to, type any other key to close:  ')

        if cont == '1':
            ongoing = True
        else:
            print("Thanks for using the app!!!")
            ongoing = False


    if choice == 4:
        print('Thanks for using the app!!!')
        ongoing = False