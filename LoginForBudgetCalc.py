#Login System and Budget Calculator

import time
print('BUDGET CALCULATOR\n\n')


#Accessing login database if it exists/Creating one if it does not.
#Enter the location for your csv file (database) below
loginInformation = '....'
try:
    with open (loginInformation, 'r', encoding = 'utf8') as loginInfo:
        check = loginInfo.readline()
        
except FileNotFoundError:
    with open (loginInformation, 'w', encoding = 'utf8') as loginInfo:
        columns = 'Username' + ',' + 'Password' + ',' + '\n'
        loginInfo.write(columns)
        adminInfo = 'admin' + ',' + 'admin' + ',' + '\n'
        loginInfo.write(adminInfo)
  

#used to ensure floats or ints are provided, not strings. 
def numberVerify(number):
    verification = float(number)/1

yesList = [
    'yes',
    'ye',
    'y',
    'yeah',
    'yea',
    'yup',
    'yep',
    'sure',
    'definitely',
    'absolutely',
    'certainly',
    'of course',
    'indeed'
    ]

noList = [
    'no',
    'n',
    'nope',
    'nop',
    'nah',
    'na',
    'don\'t',
    'dont',
    'never',
    ]

safetyLoop = ''
loginLoop = ''
accountLoop = ''
passwordLoop = ''
uniqueLoop = ''
accountList = []
passwordList = []
y = 0


accountState = input('Do you have an existing account?:\n>>')

#loops through the entire login process until an existing account and accurate password is entered, or a new, unique account id and password is made. 
while loginLoop == '':
    attempt = 3
    
    if accountState.lower().strip(' ') in yesList:
        accountInput = input('Please enter your account name:\n>>')
        
        with open (loginInformation, 'r', encoding = 'utf8') as loginInfo:
            loginInfo.seek(1)
            account = loginInfo.readline()
         
            while account != '':
                accountRead = account.split(',')
                accountList.append(accountRead[0])
                passwordList.append(accountRead[1])
                account = loginInfo.readline()
            
            if accountInput not in accountList:
                print('That account cannot be found.')
                y += 1
               
                if y == 1:
                    accountStateConfirm = ''
                    
                    while accountStateConfirm.lower().strip(' ') not in yesList and accountStateConfirm.lower().strip(' ') not in noList:
                        accountStateConfirm = input('Are you sure you have an existing account?\n>>')
                        
                        if accountStateConfirm.lower().strip(' ') in yesList:
                            print('Okay then, I hope you\'re not wasting time, because time is money.')
                            y = 0
                            
                        elif accountStateConfirm.lower().strip(' ') in noList :
                            print('No worries, let\'s make an account for you.')
                            accountState = 'no'
                            y = 0
                        
                        else:
                            print('Give me a yes or a no!')
                    
            else:  
                passwordInput = input('I found your account. Please enter your password:\n>>')

                if passwordInput not in passwordList:
                    
                    #loops until correct password is entered or times out after the set number of attempts
                    while attempt !=1 and passwordInput not in passwordList:
                        print('That was incorrect', '(' + str(attempt-1), 'attempts left).')
                        passwordInput = input('Please re-enter your password:\n>>')
                        attempt -= 1
                    
                    if passwordInput in passwordList:
                        loginLoop = 'successful'
                        print('Login Successful.\nWelcome to BUDGET CALCULATOR.')
                        
                    else:
                        print('Sorry, wrong again! You have been timed out for 3 seconds.')
                        time.sleep(3)
                        print('Your time-out has concluded.')
                        
                else:
                    loginLoop = 'successful'
                    print('Login Successful.\nWelcome to budget tracker.')
                    
    elif accountState.lower().strip(' ') in noList:
        
        while accountLoop == '':
            while uniqueLoop == '':
                newAccount = input('Please provide a unique account ID. You will use this to login:\n>>')
                
                with open (loginInformation, 'r', encoding = 'utf8') as loginInfo:
                    loginInfo.seek(1)
                    account = loginInfo.readline()
                 
                    while account != '':
                        accountRead = account.split(',')
                        accountList.append(accountRead[0])
                        passwordList.append(accountRead[1])
                        account = loginInfo.readline()
                    
                    if newAccount in accountList:
                        print('Sorry, that name is already being used.')
                    
                    else:
                        confirmNewAccount = input('Please confirm the account ID:\n>>')
                        uniqueLoop = 'successful'
            
            if newAccount == confirmNewAccount: 
                print('Your account name is confirmed.')
                accountLoop = 'successful'
                
                while passwordLoop == '':
                    newPassword = input('Please provide a password. You will also use this to login:\n>>')
                    confirmNewPassword = input('Please confirm the password:\n>>')
                    
                    if newPassword == confirmNewPassword:
                        print('Password confirmed.')
                        output = newAccount + ',' + newPassword + ',' + '\n'
                        passwordLoop = 'successful'
                                        
                        with open (loginInformation, 'a', encoding = 'utf8') as loginInfo:
                            loginInfo.write(output)
                        
                    else:
                        print('Sorry, those don\'t look like they match.')
                        passwordLoop =''
                
                print('Account Creation Successful.\nWelcome to budget tracker.')
                loginLoop = 'successful'
                                    
            else:
                print('Sorry, those don\'t look like they match.')
                accountLoop =''
            
    else:
        while safetyLoop == '':
            print('I\'m sorry, I\'m not sure what you\'re trying to say! Please try again.')
            accountState = input('Do you have an exisiting account?:\n>>')
            
            if accountState in yesList or accountState in noList:
                safetyLoop = 'successful'

wantList = [
    'fun',
    'party',
    'partying',
    'going out',
    'go out',
    'leisure',
    'vacation',
    'relief',
    'peace',
    'free time',
    'freedom',
    'time off'
    ]

savingList = [
    'retirement',
    'saving',
    'education'
    ]

debtList = [
    'debt',
    'debt payment',
    'debt repayment',
    'loan',
    'loans',
    'loan payment',
    'loan repayment',
    'cc',
    'credit card',
    'credit cards',
    'credit card payments',
    'mortgage',
    'mortgage payments',
    'mortgage payment',
    'emi',
    'car loan',
    'auto loan',
    'car auto loan',
    'car payment'
    ]

verified = False

while verified == False:
    confirmationLoop = ''
    try:
        takeHome = input('What is your monthly take home income in USD?\n>>')
        numberVerify(takeHome)
        
        while confirmationLoop == '':
            confirmation = input('Your take home is $' + takeHome + '. Is this accurate?\n>>')
            
            if confirmation.lower().strip(' ') in yesList:
                verified = True
                confirmationLoop = 'successful'
                
            elif confirmation.lower().strip(' ') in noList:
                print('Alright, let\'s try again.')
                confirmationLoop = 'successful'
                
            else:
                print('I don\'t understand that. Please give me a yes or a no.')
                confirmationLoop = ''

    except ValueError:
        print('That\'s not a number. Please try again')

postDebt = takeHome
priorityLoop = ''

while priorityLoop == '':
    priority = input('What is your current budgeting priority? (Leisure/Saving/Debt Repayment)\n>>')
    budgetConfirmationLoop = ''
    
    if priority.lower().strip(' ') in savingList or priority.lower().strip(' ') in wantList:

        while budgetConfirmationLoop == '':
            loanPaymentConfirm = input('Do you have monthly loan payments?\n>>')
            
            if loanPaymentConfirm.lower().strip(' ') in yesList:
                budgetVerified = False
                
                while budgetVerified == False:
                    loanPayment = input('How much do you pay towards debt repayment, monthly?\n>>')
                    
                    try:
                        numberVerify(loanPayment)
                        postDebt = float(takeHome) - float(loanPayment)
                        budgetVerified = True
                        budgetConfirmationLoop = 'successful'
                        
                    except ValueError:
                        print('That\'s not a number. Please try again')
                
                
            elif loanPaymentConfirm.lower().strip(' ') in noList:
                print('Awesome! Let\'s move ahead.')
                budgetVerified = True
                budgetConfirmationLoop = 'successful'
                
                
            else:
                print('I don\'t understand that. Please give me a yes or a no.')
                
        if priority.lower() in wantList and postDebt == takeHome:
            budget = {'Needs': 50*float(takeHome)/100, 'Wants':40*float(takeHome)/100, 'Savings': 10*float(takeHome)/100, 'Debt Repayment': 0.0}
            
        if priority.lower() in wantList and postDebt != takeHome:
            budget = {'Needs': 50*float(postDebt)/100, 'Wants':40*float(postDebt)/100, 'Savings': 10*float(postDebt)/100, 'Debt Repayment': float(loanPayment)}
            
        if priority.lower() in savingList and postDebt == takeHome:
            budget = {'Needs': 50*float(takeHome)/100, 'Wants':20*float(takeHome)/100, 'Savings': 30*float(takeHome)/100, 'Debt Repayment': 0.0}
            
        if priority.lower() in savingList and postDebt != takeHome:
            budget = {'Needs': 50*float(postDebt)/100, 'Wants':20*float(postDebt)/100, 'Savings': 30*float(postDebt)/100, 'Debt Repayment': float(loanPayment)}
            
        priorityLoop = 'successful'
            
    elif priority.lower().strip(' ') in debtList:
        
        budgetVerified = False
        
        while budgetVerified == False:
            loanPayment = input('How much do you pay towards debt repayment, monthly?\n>>')
            
            try:
                numberVerify(loanPayment)
                postDebt = float(takeHome) - float(loanPayment)
                budgetVerified = True
                budgetConfirmationLoop = 'successful'
                
            except ValueError:
                print('That\'s not a number. Please try again')
            
        budget = {'Needs': 50*float(postDebt)/100, 'Wants':10*float(postDebt)/100, 'Savings': 40*float(postDebt)/100, 'Debt Repayment': float(loanPayment)}
        
        priorityLoop = 'successful'
        
    else:
        print('I don\'t understand that! Try using one of the suggestions from the brackets in the following prompt.')

#if income post debt is negative, provide alternative solutions. 
if float(postDebt) > 0:
    print('After considering your income, priorities, and debt, the following is your suggested budget:')
    print(budget)
    print('Best of luck on your financial journey!')
    
else:
    print('Your income, post debt, is negative. I don\'t think I\'m qualified to help you. This video may be more helpful!')
    print('https://www.youtube.com/watch?v=xvFZjo5PgG0')
    
             
