def isnumber(s):
    'returns True if string s can be transformed to an integer'
    s = s.strip() # remove any whitespaces before/after number
    if s == '':
        return False
    if s[0] == '-':
        s = s[1:] # cut-off minus sign and check if the remainder is empty
        if s == '':
            return False
    for c in s: # check if every character of the remainder is a digit 
        if c<'0' or c>'9':
            return False
    return True

# tests: function calls 
print(isnumber('2'))
print(isnumber('  -10'))
print(isnumber('-29484792364'))
print(isnumber('2974290 '))
print(isnumber(''))
print(isnumber('-'))
print(isnumber('--2'))
print(isnumber('2a74290'))
