

def hash(key_string):
    hsh = 0
    for char in key_string:
        hsh += ord(char)
    return hsh % 100


print(hash('123456-A'))
