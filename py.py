import random 

x = random.randrange(1000,9999)

print(x)

y = int(input("cislo: "))

if len(str(y)) == 1 and str(y) in str(x):
    for i in (y):
        if y == i :
            print(i)