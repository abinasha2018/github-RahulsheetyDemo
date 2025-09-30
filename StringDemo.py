str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"


print(str[1]) #a
# if you want substring in python
print(str[0:5]) #Rahul

print(str+str1) # concatenation

#Check string is present in another string..
print(str3 in str) # True #Substring check


var=str.split(".")
print(var) #['RahulShettyAcademy', 'com']
print(var[0])  #RahulShettyAcademy

str4 = " great  "
#Strip is method used to trim white spaces in the beginning and at the end
print(str4.strip()) #great

# Remove the left or beginning whitespaces
print(str4.lstrip())

## Remove the Right or Last whitespaces

print(str4.rstrip())








