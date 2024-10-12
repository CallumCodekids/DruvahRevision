#VARIABLES are how we get the computer to keep track of information for us
#each VARIABLE has a NAME and a VALUE
#the NAME of a VARIABLE should start with (and contain only) lower case letters and underscores.
#A VARIABLE NAME can contain but cannot start with DIGITS (0-10)
#A VARIABLE NAME should be no more than 3 words long and describe the purpose of the VARIABLE and the meaning/relevance of its VALUE
#to create a VARIABLE, write a NAME, and equals sign, and a VALUE
#to access the VALUE of a VARIABLE, write just the NAME of the variable
#to modify the VALUE of a VARIABLE, write the name of the VARIABLE, and equals sign, and the new VALUE you wish it to contain
#VARIABLES can be thought of as boxes containing information, the NAME of the VARIABLE is the label on the box
#The VALUE of the VARIABLE is what is inside the box

#without running it, can you work out what the following code outputs?:

a = 3
b = 5
c = a + b
b = a + c
a = b + c
print(a)
print(b)
print(c)
c = (a + b) * c
print(c)