import time
import random
import board
import neopixel
import random
import touchio
from ncount import *


touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

from aure import *

sayings = ["live long and prosper","may the force be with you","size matters not"]

while True:
    saying = random.choice(sayings)
    print(saying)
    blinknum(2,green)
    doAure(saying)
    compthink()
    time.sleep(2)
