import string
from random import *
max_char = 12
password = "".join(choice(string.ascii_letters) for x in range(randint(12, max_char)))
print ("This is your password : ",password)