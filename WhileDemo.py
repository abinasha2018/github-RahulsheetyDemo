it = 4

while it>1:
    if it !=3:
        print(it)
    it = it -1

print("While loop execution is done")


#break
it = 4

while it>1:
    if it ==3:
        break
    print(it)
    it = it -1

print("While loop execution is done")


#Continue
it = 10

while it>1:
    if it ==9:
        it = it -1
        continue
    if it ==3:
        break
    print(it)
    it = it -1

print("While loop execution is done")






