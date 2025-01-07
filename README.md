# Aurebesh

* Using a modified Figlet font ("standard.flf") I created aurebesh.flf, replacing a-z in the font with Aurebesh symbols.
* I extracted the text for the a-z from Aurebesh.flf and made them into an array of texts for aure.py
* aure.py has a function doAure(text,delay,REPL) - text =  the text to display in Aurebesh, delay is how long between each letter, and REPL indicates if the output is to go to the REPL or, via HID, out as keyboard input.

* aurebesh.py is a CircuitPython program that uses prt.py and ncount.py. Touching pad#1 will deliver one-by-one the alphabet, touching #2 will choose a random saying from sayings[] and print the English version, then the Aurebesh letters, one-by-one.

  
