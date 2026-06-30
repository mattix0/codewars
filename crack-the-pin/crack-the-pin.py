'''
Given is a md5 hash of a five digits long PIN. It is given as string. Md5 is a function to hash your password: "password123" ===> "482c811da5d5b4bc6d497ffa98491e38"
Why is this useful? Hash functions like md5 can create a hash from string in a short time and it is impossible to find out the password, if you only got the hash. The only way is cracking it, means try every combination, hash it and compare it with the hash you want to crack. (There are also other ways of attacking md5 but that's another story) Every Website and OS is storing their passwords as hashes, so if a hacker gets access to the database, he can do nothing, as long the password is safe enough.

Your task is to return the cracked PIN as string.

This is a little fun kata, to show you, how weak PINs are and how important a bruteforce protection is, if you create your own login.
'''

from hashlib import md5
def crack(hash):
    for i in range(100000):
        pin = f'{i:05d}'
        if md5(pin.encode()).hexdigest() == hash:
            return pin

## Tests
crack("827ccb0eea8a706c4c34a16891f84e7b"), "12345"
crack("86aa400b65433b608a9db30070ec60cd"), "00078"