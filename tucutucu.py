import random
pp = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ohno = int(input("longitud de contraseña por favor: "))
ohno_tucu = ""
for i in range(ohno):
    ohno_tucu += random.choice(pp)

print(ohno_tucu)
