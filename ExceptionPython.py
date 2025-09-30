
ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    # raise Exception("Produces Cart count not matching")
    pass

assert (ItemsInCart == 0) ,"Products Cart count not Matching"


#try , catch
try:
    with open('text.txt','r') as reader:
        reader.read()
except:
    print("Somehow i reached this block because there is failure in try block")

#Customize Exception Message

try:
    with open('text.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Cleaning up resources")

