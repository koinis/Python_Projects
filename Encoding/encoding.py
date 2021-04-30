def shiftRightLower(c,key):
	word = ord('a')+(ord(c)-ord('a')+key)%26	
	return chr(word)
    
def shiftLeftLower(c,key):
	word = ord('a')+(ord(c)-ord('a')-key)%26	
	return chr(word)

def shiftRightUpper(c,key):
	word = ord('A')+(ord(c)-ord('A')+key)%26	
	return chr(word)

def shiftLeftUpper(c,key):
	word = ord('A')+(ord(c)-ord('A')-key)%26	
	return chr(word)


# Examples
print(shiftRightLower('a',3))
print(shiftRightLower('x',10))
print(shiftLeftLower('d',3))
print(shiftLeftLower('h',10))
print(shiftRightUpper('A',3))
print(shiftRightUpper('X',10))
print(shiftLeftUpper('D',3))
print(shiftLeftUpper('H',10))



# does not encode characters not in the latin alphabet
def encodetext(s,key):
	import string
	sout = ''
	for c in s:
		if c in string.ascii_lowercase:
			sout += shiftRightLower(c,key)
		elif c in string.ascii_uppercase:
			sout += shiftRightUpper(c,key)
		else:
			sout += c
	return sout
    


# does not decode characters not in the latin alphabet
def decodetext(s,key):
	import string
	sout = ''
	for c in s:
		if c in string.ascii_lowercase:
			sout += shiftLeftLower(c,key)
		elif c in string.ascii_uppercase:
			sout += shiftLeftUpper(c,key)
		else:
			sout += c
	return sout

coded = encodetext('Hello, World! How are you?',10)
print(coded)
decoded = decodetext(coded,10)
print(decoded)
