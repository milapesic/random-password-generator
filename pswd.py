import string
import random


letters=list(string.ascii_lowercase+string.ascii_uppercase)
numbers=list(string.digits)
special=list(string.punctuation)
char=list(string.ascii_letters+string.digits+string.ascii_lowercase+string.ascii_uppercase+string.punctuation)
random.shuffle(char)


d=0
while True:
    try:
        d=int(input('Please enter the length of your password. It has to be at least 8: '))
        if d<8:
            print('Invalid input! Password is too short. It has to be at least 8 characters long. ')
            continue
        l=int(input('How many letters would you like: '))
        n=int(input('How many numbers would you like: '))
        s=int(input('How many special characters would you like: '))
        total=l+n+s
        if total>d:
            print('Invalid input! Total number of characters is longer than the input length.')
            continue
    except ValueError:
        print('Invalid input! Please enter a number.')
        continue
    else:
        if d>=8:
            psw=[]   
            for i in range (int(l)):
                psw.append(random.choice(letters))
            for i in range (int(n)):
                psw.append(random.choice(numbers))
            for i in range (int(s)):
                psw.append(random.choice(special))    
            for i in range(d-total):
                psw.append(random.choice(char))

            print("".join(psw))
        
        else:
            print('It cannot be less than 8 characters long')
            continue