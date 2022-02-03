




import os 
def decorator(func):
    def wrapper():
        func()
        print(os.getcwd())
    return wrapper



@decorator
def file_maker():
    with open('latter.txt','w') as f:
        f.write('Hello dear \n')
        f.write('I hope you ok. I m wrote a little latter for one reason: \n')
        f.write('I invite u to my party birthday to celebrate with my friends and family. \n')
        f.write('the address is in avenue lincoln number 14 in newark \n')
        f.write('Atte: Max')
        
file_maker()