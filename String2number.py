def str2num(s):
    out = ""
    for x in s:
        ASCII = ord(x.upper())
        out += str(ASCII)
    return int(out)


def num2str(m):
    out = ""
    s = str(m) 
    for i in range(len(s)/2): 
        aba = s[2*i] + s[2*i+1]
        out += chr(int(aba))
    return out

def remove_punctuation(s):
    punct = [".",",","?","!","'",'"',":",";","-","(",")","[","]"," "]
    out = ""
    for i in s:
        if i.isalpha():
            out += i.upper()
        elif i in punct:
            continue
        else:
            return 'Invalid input'
    return out
