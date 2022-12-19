import logging
logging.basicConfig(level=logging.DEBUG,filename='sumlogger.log')

def sumnum(*args):
    logging.debug(args)
    add=0
    for i in args:
        add=add+i
    return add

a=sumnum(1,2,3,4,5,6,7,8,9)

with open('sumlogger.log','r') as f:
    print(f.read())
