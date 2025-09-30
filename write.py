# file = open("text.txt")
# file.close()

# Or

#This particular line open the file once the whole execution completed it will just closed
#read the file and store all the lines in list
#reverse the list
#write the list back to the file
with open ('text.txt' , 'r') as reader:
    contents = reader.readlines() #['abc\n', 'bvdfg\n', 'cat\n', 'dog\n', 'elephant']
    reversed(contents)
    with open('text.txt', 'w') as writer:
        for line in reversed(contents):
            writer.write(line)


