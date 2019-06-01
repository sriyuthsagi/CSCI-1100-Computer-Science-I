
#input password
password = input('Enter a password => ')
print(password)



#Rule 1
if len(password) <= 25 and len(password) >= 10 and password[0].isalpha():
    print('Rule 1 is satisfied')
    rule1 = True
else:
    print('Rule 1 is not satisfied')
    rule1 = False



#Rule 2
if '@' in password or '$' in password:
    if '%' not in password:
        print('Rule 2 is satisfied')
        rule2 = True
    else:
        print('Rule 2 is not satisfied')
        rule2 = False
else:
    print('Rule 2 is not satisfied')
    rule2 = False
    


#Rule 3
if not password.islower() or password.isupper():
    print('Rule 3 is satisfied')
    rule3 = True
elif '1' in password or '2' in password or '3' in password or '4' in password:
    print('Rule 3 is satisfied')
    rule3 = True
else:
    print('Rule 3 is not satisfied')
    rule3 = False
    


#Rule 4
rule4 = True
for i in range(len(password)-1):
    if password[i].isupper():
        if not password[i+1] == '_':
            rule4 = False
            break
if password[len(password)-1].isupper():
    rule4 = False
if rule4:
    print('Rule 4 is satisfied')
else:
    print('Rule 4 is not satisfied')



#Rule 5
if '5' in password or '6' in password or '7' in password or '8' in password or '9' in password or '0' in password:
    print('Rule 5 is not satisfied')
    rule5 = False
else:
    print('Rule 5 is satisfied')
    rule5 = True
    
    

#password suggestion
if rule1 and rule2 and rule3 and rule4 and rule5:
    print('The password is valid')
elif not rule1:
    pass
else:
    npassword = password[0:8] + '42' + password[(len(password)-8):len(password)]
    print('A suggested password is', npassword)


