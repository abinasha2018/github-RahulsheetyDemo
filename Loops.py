greeting = "Good Morning"

if greeting == "Good Morning":
    print("Hello if block executed sucessfully")
    print("Second line")
else:
    print("Else block executed sucessfully")

print("This is not if-lese block")



#For loop

obj = [2,3,5,7,9]

for i in obj :
    print(i)
    # print(i*2)

print("--------------------------------------------------------------")


#Sum of First Natural numbers  1+2+3+4+5 = 15
su = 0
for j in range(1,6):# range(i,j) -> i to j-1
    su = su+j

print(su)


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
sum=0
for i in range(1,10,2):
    sum =sum+i
print(sum)

print("----------------------------------------------------------------")

numbers =[]

for i in range(10):
    numbers.append(i)
print(numbers)


for number in numbers:
    print(number)


