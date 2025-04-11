hello = input('Hello! My name is Stella. What is your name?')
greet = print('Nice to meet you', hello)
number = input('Can you choose a number for me? From 0-5')
number2 = int(number)
guesswhat = [cat, flower, potato, book, zebra]
guess = guesswhat[number2]
print('Now we will start! I am a', guess)

amI = input('Am I an animal?')
if amI == 'yes':
    amI2 = input('Am I a cat')
    if amI2 == 'yes':
        print('Horray! I am a cat. Thank you for playing. MEOW-MEOW-MEOW!')
    else:
        amI3 = print('Am I a zebra?')
        if amI3 == 'yes':
            print('Horray! I am a zebra. Thank you for playing.')
        else:
            print('Uh-oh. Something went wrong')
        