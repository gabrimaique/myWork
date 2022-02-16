numberToguess = 30
guess = int(input('please guess the number:'))
while guess != numberToguess:
    print('wrong')
    guess = int(input('please guess again:'))
    print('well done! yes the number was', numberToguess)