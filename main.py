from ideaboard import IdeaBoard
from interpreter import Interpreter
from time import sleep_ms

rb = IdeaBoard()
inter = Interpreter()

#define functions (using non just to get a None parameter)
def redColor(non):
    rb.pixel((255,0,0))
    
def blueColor(non):
    rb.pixel((0,0,255))
    
def noColor(non):
    rb.pixel((0,0,0))

# add functions to interpreter ('name', (function, parameter))
inter.addFunction('sleep1000',(sleep_ms,1000))
inter.addFunction('sleep100',(sleep_ms,100))
inter.addFunction('redColor',(redColor,None))
inter.addFunction('noColor',(noColor,None))
inter.addFunction('blueColor',(blueColor,None))



while True:
    inter.execute('redColor:sleep1000:noColor:sleep100:blueColor:sleep1000')
