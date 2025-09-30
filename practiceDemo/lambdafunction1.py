
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x:x*2,numbers)
print(list(doubled_numbers))

even_numbers = list(filter(lambda x:x%2==0,numbers))
print(even_numbers)


num =[3,2,6,1,4,5]
sorted_num = sorted(num)
print(sorted_num)