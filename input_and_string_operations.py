#the INPUT FUNCTION is very similar to the print function in that it also outputs the text inside of it to the terminal
#however, unlike the print function the INPUT FUNCTION
#takes only a single STRING as an argument, rather than any number of any values
#asks the string as a question to the user and BLOCKS the execution of the rest of the program until the question has been answered
#by tying in the terminal and hitting enter
#and RETURNS the answer to the question as a string, making the call to the INPUT FUNCTION produce the answer as a value after the input function has finished execution
#if you wish to use the result of the input function as not-a-string (ie, an integer or a boolean), or include the value of a non-string in a call to INPUT you will need to CAST it to the appropriate TYPE
#to cast a value to a different TYPE, type the short name of the desired VALUE TYPE, then parentheses, and the VALUE to be transformed inside of the parentheses
#ie str() converts to strings, bool() converts to booleans, int() converts to integers
#if the value inside of the parentheses cannot be CAST to the desired TYPE, attempting to CAST IT will cause a runtime error
#STRINGS can be concatenated (added to the end of each other) using the + OPERATOR and duplicated using the * OPERATOR
name = input("Hi, what's your name?: ")
print("Hi",name)#print takes multiple parameters, we can use a comma to seperate them
num_icecreams = input(name + " how many icecreams do you want?: ")#input takes only a single string as a parameter, we need to use + to concatenate the values we want to output into a single string
num_icecreams = int(num_icecreams) #if the answer was anything other than a valid python integer this will cause a runtime error
print("Here you go 😁: ", "🍨"*num_icecreams)
print("I'm having some too 😋 ", "🍨"*(num_icecreams+1))