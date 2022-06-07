number = input('Phone number: ')
dutch = ('+31')
german = ('+49')
belgian = ('+32')
if dutch in number:
    print('You have a dutch phone number ' + number)
if german in number:
    print('You have a german phone number ' + number)
if belgian in number:
    print('You have a belgians phone number ' + number)