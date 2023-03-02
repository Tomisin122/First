import random

tomi = ""
soni = []
while len(soni) < 4:
    use = random.randint(0,9)

    soni.append(use)
for i in soni:
    tomi += str(i)
print(tomi)
