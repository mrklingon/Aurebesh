import time
import random
import board
import neopixel
import random
import touchio
from ncount import *
from prt import *


touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

from aure import *

sayings = ["live long and prosper","may the force be with you","size matters not"]

REPL = True #True for use in IDE, False for printing via HID. Will blink red until you touch 1 or 2


compthink()

if REPL == False:
    Val=0
    while Val==0:
        blinknum(1,red)
        if touch1.value:
            Val = Val + 1
        if touch2.value:
            Val = Val + 2
    

#touch 1 for Aurebesh alphabet, 2 for random saying in Aurebesh.

while True:
    Val = 0
    
    if touch1.value:
        Val = Val + 1
        
    
    if touch2.value:
        Val = Val + 2
    if Val == 2:
        saying = random.choice(sayings)
        prt(saying,REPL)
        blinknum(2,green)
        doAure(saying,.1,REPL)
        compthink()
    if Val == 1:
        for i in range(26):
            l=(chr(ord("a")+i))
            prt(l,REPL)
            doAure(l,.25,REPL)
            
    time.sleep(.1)
