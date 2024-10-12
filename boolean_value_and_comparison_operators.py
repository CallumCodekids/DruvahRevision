#BOOLEANs are a data type which can hold a value of either True or False
#they are produced by (among other things) COMPARISON OPERATORS and used for (among other things) CONTROL FLOW in python
#the basic COMPARISON OPERATORS are
# ==, which checks if the two values on either side of it are the same and produces a value of True if they are or False if they're not
# >, which checks if the value on the left is greater than the value on the right, and produces a value of True if they are and False if they're not
# < which checks if the value on the left is less than the value on the right, and produces a value of True if they are and False if they're not
# >= and <= which work as above but produce a value of True not False if the values on either side are equal

print(5 == 5)
print(55 == 5)
print(5 == 5.0)
print(5 == 5.1)
print(5 == 5.000000000000000000000001) #watch out for floating point error, python only actually stores decimal numbers to about 12 decimal place precision,
print(5 == "5")
print("5" == "5")
print("cat" == "dog")
print("Cat" == "cat")
print("cat " == "cat")
print("cat"== "cat")

print(5 > 6)
print(5 > 7)
print(5 > 5)
try:
    print(5 > "banana is yummi in me tummi") #Runtime Error
except:
    print("oops!")

print(5 > 5.1)
print(5 > 4.9)
print(5 > 4.99999999999999999999999999999999999999999999999999999999)
print(5 < 4)
print(5 < 5)
print(5 < 6)
print(5 >= 4)
print(5 >= 5)
print(5 >= 6)