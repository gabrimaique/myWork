# This program reads in a students percentege
# and prints out the corresponding grade

percentege = float(input('enter the percentege:'))

if percentege < 0 or percentege > 100:
    print ('please enter a number between 0 and 100')
    
    
elif percentege < 40:
        print ('fail')
elif percentege < 50:
        print ('pass')
elif percentege < 60:
        print ('merit1') 
elif percentege < 70:
        print ('merit2') 
else:
        print('distinction')    
