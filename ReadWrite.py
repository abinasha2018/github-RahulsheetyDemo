#Read the file

file = open("text.txt")

#Read all the contents of file
# print(file.read())

#it only pick first two character
#Read n number of character by passing parameter
# print(file.read(2))

#read one single line at a time readline()
# print(file.readline())
# print(file.readline())


#print all the contents of the file line by line using readline() method
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()


# Or
#Store the data into a list like this['abc\n', 'bvdfg\n', 'cat\n', 'dog\n', 'elephant']
# print(file.readlines())

#Print the list value one by one
for line in file.readlines():
    print(line)


file.close()