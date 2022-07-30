import random
passlen = int(input(" length of password"))

s = '''abcdefghjiklmnopqrstuvwxyz
0123456789
ABCDEFGHIJKLMNOPQRSTUVWXYZ
!@#$%^&*()?'''

p = "".join(random.sample(s,passlen))
print(p)
