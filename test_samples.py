import String2number
def encrypt_caesar(s, key):
    alphabet1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    alphabet2 = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabet = alphabet1 + alphabet2
    l = len(key)
    s_new = String2number.remove_punctuation(s)
    if type(s) != str:
        return 'Invalid input'
    if type(key) != str:
        return 'Invalid input'
    if l != 1:
        return 'Invalid input'
    if s_new == 'Invalid input':
        return 'Invalid input'
    output = ''  
    for i in s_new:
        if i == ' ':
            output += i
            continue
        shift = alphabet.index(key)
        ic = (alphabet.index(i) + shift) % len(alphabet)
        output += alphabet[ic]
    return output

def decrypt_caesar(s, key):
    alphabet1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    alphabet2 = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabet = alphabet1 + alphabet2
    l = len(key)
    s_new = String2number.remove_punctuation(s)
    if type(s) != str:
        return 'Invalid input'
    if type(key) != str:
        return 'Invalid input'
    if l != 1:
        return 'Invalid input'
    if s_new == 'Invalid input':
        return 'Invalid input'
    output = ''
    shift = alphabet.index(key)
    for i in s_new:
        if i == ' ':
            continue
        si = alphabet.index(i) - shift
        if si < 0:
            si = si + len(alphabet)
        output += alphabet[si]
    return output

def generate_key(s, key):
    key = list(key)
    if len(s) == len(key):
        return ("".join(key))
    else:
        for i in range(len(s) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

def encrypt_vigenere(s, key):
    alphabet1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    alphabet2 = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabet = alphabet1 + alphabet2
    key = generate_key(s, key)
    s1 = String2number.remove_punctuation(s)
    k1 = String2number.remove_punctuation(key)
    l = len(key)
    out = []
    if type(s) != str:
        return 'Invalid input'
    if type(key) != str:
        return 'Invalid input'
    if s1 == 'Invalid input':
        return 'Invalid input'
    if k1 == 'Invalid input':
        return 'Invalid input'
    if l == 0:
        return 'Invalid input'
    for i in range(len(s1)):
        ic = (ord(s1[i]) + ord(k1[i])) % 26
        ic += ord("A")
        out.append(chr(ic))
    return ("".join(out))

def decrypt_vigenere(s, key):
    key = generate_key(s, key)
    s1 = String2number.remove_punctuation(s)
    k1 = String2number.remove_punctuation(key)
    l = len(key)
    output = []
    if type(s) != str:
        return 'Invalid input'
    if type(key) != str:
        return 'Invalid input'
    if s1 == 'Invalid input':
        return 'Invalid input'
    if k1 == 'Invalid input':
        return 'Invalid input'
    if l == 0:
        return 'Invalid input'
    for i in range(len(s1)):
        si = (ord(s1[i]) - ord(k1[i]) + 26) % 26
        si += ord("A")
        output.append(chr(si))
    return ("".join(output))


class DH_cipher(object):
    def __init__(self, Alice_pub_key, Bob_pub_key, private_key):
        self.Alice_pub_key = Alice_pub_key
        self.Bob_pub_key = Bob_pub_key
        self.private_key = private_key
        self.common_key = None
        
    def get_partial_key(self):
        part_key = self.Alice_pub_key ** self.private_key
        part_key = part_key % self.Bob_pub_key
        return part_key
    
    def get_common_key(self, part_key_r):
        common_key = part_key_r ** self.private_key
        common_key = common_key % self.Bob_pub_key
        self.common_key = common_key
        return common_key
    
    def encrypt(self, message):
        encrypt_message = ""
        key = self.common_key
        for i in message:
            encrypt_message += chr(ord(i) + key)
        return encrypt_message
    
    def decrypt(self, encrypt_message):
        decrypt_message = ""
        key = self.common_key
        for j in encrypt_message:
            decrypt_message += chr(ord(j) - key)
        return decrypt_message
    

def fib(N):
    f = [0, 1]
    for i in range(2, N+1):
        f.append(f[i - 1] + f[i - 2])
    return f[N]

def all_fib(N):
    return [fib(i) for i in range(1, N + 1)]

def test_answer():
    assert encrypt_caesar("A cat!", "B") == 'BDBU'
    assert encrypt_caesar("This is Yang", "L") == 'ESTDTDJLYR'
    assert encrypt_caesar("Have a good day", "No<No>") == 'Invalid input'
    assert encrypt_caesar("Not <good>", "A") == 'Invalid input'
    assert encrypt_caesar("final week", "ABC") == 'Invalid input'

    assert decrypt_caesar(" Hello", "OK") == 'Invalid input'
    assert decrypt_caesar('XLMW MWEJ YRXM QI', "E") == 'THISISAFUNTIME'
    assert decrypt_caesar("Hello", "key") == 'Invalid input'
    assert decrypt_caesar("SVYFOMYQC", "K") == 'ILOVECOGS'
    assert decrypt_caesar("rain <@", "M") == 'Invalid input'

    assert generate_key("MATH", "Hi") == "HiHi"
    assert generate_key("Hello", "ABCDE") == "ABCDE"
    assert generate_key("Please", "A") == 'AAAAAA'

    assert encrypt_vigenere("What a wonderful word","key") == 'GLYDEUYRBOVDEPUYVB'
    assert encrypt_vigenere("Math is fun and cool!","ORANGE") == 'ARTUOWTLNNTHQFOY'
    assert encrypt_vigenere("hello, <world>", "hi") == 'Invalid input'
    assert encrypt_vigenere("I feel tired now", "What>") == 'Invalid input'

    assert decrypt_vigenere('GLYDEUYRBOVDEPUYVB', "key") == "WHATAWONDERFULWORD"
    assert decrypt_vigenere("hello <@ hi", "Nice") == 'Invalid input'
    assert decrypt_vigenere('Nobody here', "fail@") == 'Invalid input'
    assert decrypt_vigenere('KFHZGGRGCNL', "cute") == "ILOVEMYCATS"

    Alice_pub_key = 5
    Bob_pub_key = 6
    private_key = 2
    test_DH = DH_cipher(Alice_pub_key, Bob_pub_key, private_key)
    test_DH.get_common_key(8)
    assert test_DH.encrypt("Hello world") == 'Lipps${svph'
    assert test_DH.decrypt('Tmk') ==  'Pig'

    assert fib(1) == 1
    assert fib(4) == 3
    assert fib(100) == 354224848179261915075

    assert all_fib(3) == [1, 1, 2]
    assert all_fib(100)[-1] == fib(100)
    assert type(all_fib(9)) == list
    assert type(all_fib(9)[2]) == int


