# Aurebesh

![table of Aurebesh alphabet](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Star-Wars-aurek-besh-alphabet-chart.svg/320px-Star-Wars-aurek-besh-alphabet-chart.svg.png)

* Using a modified Figlet font ("standard.flf") I created aurebesh.flf, replacing a-z in the font with Aurebesh symbols.
* I extracted the text for the a-z from Aurebesh.flf and made them into an array of texts for aure.py
* aure.py has a function doAure(text,delay,REPL) - text =  the text to display in Aurebesh, delay is how long between each letter, and REPL indicates if the output is to go to the REPL or, via HID, out as keyboard input.

* aurebesh.py is a CircuitPython program that uses prt.py and ncount.py. Touching pad#1 will deliver one-by-one the alphabet, touching #2 will choose a random saying from sayings[] and print the English version, then the Aurebesh letters, one-by-one.

  **Notes:**

Edit the variable REPL in aurebesh.py to True for text to show up in the REPL; make it False for text to be delivered as if typed. Edit the variable "sayings" to the list of sayings you want to display in Aurebesh.

**Files** (copy these all to your neotrinkey)
* ncount.py
* aure.py
* prt.py
* aurebesh.py -- copy this to "code.py"

If output is going as if typed, the program will pause when started, blinking red till you touch one of the pads - this gives you a chance to move the cursor to the window you wish to receive the output.

**Info:**

Figlet: https://en.wikipedia.org/wiki/FIGlet
Aurebesh: https://starwars.fandom.com/wiki/Aurebesh
