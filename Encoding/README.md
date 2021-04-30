# Encoding

This is a Python encoding program.

The program consists of two basic functions, the function encodetext and the function decodetext.
The program also includes four help functions which are used in the implemetation of encodetext and decodetext.

## help functions
shiftRightLower(c,key) = Takes a lowercase letter "c" as an argument and returns the lowercase letter located "key" positions after "c" in the English alphabet.

shiftRightUpper(c,key) = Takes a lowercase letter "c" as an argument and returns the lowercase letter located "key" positions before "c" in the English alphabet.

shiftRightUpper(c,key) = Takes an uppercase letter "c" as an argument and returns the uppercase letter located "key" positions after the uppercase letter "c" in the English alphabet.

shiftLeftUpper(c,key) = Takes an uppercase letter "c" as an argument and returns the uppercase letter located "key" positions before the uppercase letter "c" in the English alphabet.


## basic functions
The function encodetext, encodes by using the shifting of the letters which includes. 
(Uses the help functions shiftRightLower(c,key) and shiftRightUpper(c,key)).

For example the call of encodetext('Hello, World! How are you?',10) should returns 'Rovvy, Gybvn! Ryg kbo iye?'


The function decodetext, decodes a text
(Uses the help functions shiftLeftLower(c,key) and  shiftLeftUpper(c,key)).

For example the call of decodetext('Rovvy, Gybvn! Ryg kbo iye?',10) should returns 'Hello, World! How are you?'
