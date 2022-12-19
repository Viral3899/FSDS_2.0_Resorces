# import logging

# logging.basicConfig(level=logging.INFO)

# def addition(x,y):
#     return x+y

# def substract(x,y):
#     return x-y

# def multiply(x,y):
#     return x*y

# def divide(x,y):
#     return x/y

# n1=50
# n2=20

# res_add=addition(n1,n2)
# logging.info(res_add)
# res_sub=substract(n1,n2)
# logging.info(res_sub)
# res_mul=multiply(n1,n2)
# logging.info(res_mul)
# res_div=divide(n1,n2)
# logging.info(res_div)



import logging

logging.basicConfig(filename='new.txt',level=logging.DEBUG)
    

def namecheck():
    name=input('Enter The Name : ')
    if len(name)<2:
        logging.debug('Enter The Name having 2 or More character')
        return 'Invalid Name'
    elif name.isspace():
        logging.debug('you Entered Only Space')
        return 'Invalid Name'
    elif name.isalpha():
        logging.debug('Your Name is having Alphabets')
        return 'Valid Name'
    elif name.replace(' ','').isalpha():
        logging.debug('Your Name is having Alphabets & Space')
        return 'Valid Name'
    else:
        logging.debug('Failed to Check all condition')
        return 'Try Again You name is Invalid'


namecheck()