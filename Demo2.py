# values =[1,2,3,"Rahul",4,4.5]
# #List is a datatypes that allows multiple values and can be different data types
#
# print(values[0])  #1
#
# print(values[3]) #"Rahul"
#
# # if i want to print the last number
# print(values[-1]) #4.5
#
# print(values[1:3]) #2,3
#
# values.insert(4,"Shetty")
# print(values) #[1, 2, 3, 'Rahul', 'Shetty', 4, 4.5]
#
# values.append("End")
# print(values) #[1, 2, 3, 'Rahul', 'Shetty', 4, 4.5, 'End']
#
# values[3] = "RAHUL" #Updating
# print(values) #[1, 2, 3, 'RAHUL', 'Shetty', 4, 4.5, 'End']
#
# del values[0]
# print(values) #[2, 3, 'RAHUL', 'Shetty', 4, 4.5, 'End']


#Tuple
# Same as list datatype but immutable

# val = (1,2,"rahul",4.5)
# print(val[1])

#Assinging not possible in tuple
# val[2] = "RAHUL"
# print(val)


#Dictionary

# dic ={"a":2,4:"bcd","c":"Hello world"}
# print(dic)
# print(dic["c"])

#Add key value pair run time
dict={}

dict["Firstname"] ="Rahul"

dict["Lastname"] = "Shetty"

dict["Gender"] ="Male"
print(dict)

print(dict["Gender"])












