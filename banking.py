import random

database = {}


def init():


    
    
    print ( "welcome to bank of carribean")
    print('             ')

    

    haveAccount = int(input ('do you have an account with us: 1. yes 2. no \n'))

    

    if (haveAccount == 1):
            
        login()
    elif(haveAccount == 2):
           
        register()
    else:
        print ('invald option selected')
        init()


def login():
    print ("login to your account  " )

    userAccountNumber = int(input('enter your account number \n'))
    password = input('enter your password \n')
    

    for accountnumber, userDetails in database.items():
        if(accountnumber == userAccountNumber):
            if(userDetails[3] == password):                
                  bankOperation(userDetails)

    print ('invalid ccount or password')
    login()

def register():
    
    print ('register with us here')
    print('             ')
    
    email = input("Please enter a valid email address \n")
    first_name = input ('enter your first name all in block \n')
    last_name = input ('enter your last name all in block \n')
    password = input ('choose a password \n')

    accountnumber = generateAccount()

    database[accountnumber] = [ first_name, last_name, email, password ]

    print ("your account has been created")
    print (' ')
    print('your account account number is %d' % accountnumber)
    print('             ')
    print('keep your ccount details safe')
    print(' ')

    login()

def bankOperation(user):
    
    print ("welcome to bank of carribean %s %s " % (user[0], user [1]))
    
    selectedOption = int(input('what would you like to do? 1 deposit 2. withdrawal 3. logout 4. exit \n'))

    if(selectedOption == 1):
          
        depositOperation()
    elif(selectedOption == 2):
       
        withdrawalOperation()
    elif(selectedOption == 3):
       
        logout()
    elif(selectedOption == 4):
          
        exit()
    else:
        print('you selected an invalid option')
        bankOperation(user)
            
        
        
def withdrawalOperation():
    withdrawal = int(input('How much would you like to withdraw \n'))
    if (withdrawal >= 1):
                             
        print ('take your cash')
        print('             ')
        print('thank you for banking with us')
        print('             ')
        logout() 
    else:
        print('enter an amount greater than 0')
        bankOperation(user)

def depositOperation():
    deposit = int(input('How much would you like to deposit? \n'))
            
    print('your current balance is %s' % deposit)
    print('             ')
    print('thank you for banking with us')
    print('             ')

    logout()
    

def generateAccount():
        
        return random.randrange(0000000000,9999999999)

def logout():
    login()

    
init()



