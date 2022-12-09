from email_validator import validate_email, EmailNotValidError

mail = input('Please enter your Email-Address: ')


def check(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print(str(e))


sliced_mails = {}


def slicer(mail):
    mailcheck = check(mail)
    while mailcheck != True:
        mail = input('please re-enter a valid email: ')
        mailcheck = check(mail)
    userdom = mail.split('@')
    username = userdom[0]
    domain = userdom[1]
    sliced_mails[mail] = [username, domain]
    print(f'Your username is: {username}\nYour domain name is: {domain}')
    nxtact = input('Do you want to slice more mails?\n')
    if nxtact.lower() == 'yes':
        mail = input('Enter an Email-Address: ')
        slicer(mail)
    else:
        mails = list(sliced_mails.keys())
        print(f'{len(sliced_mails)} mails have been sliced')
        [print(f'{i}\nUsername: {sliced_mails[i][0]}\nDomain: {sliced_mails[i][1]}\n------------') for i in mails]

slicer(mail)