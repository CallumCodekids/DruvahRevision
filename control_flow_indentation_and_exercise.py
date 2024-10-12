#IF STATEMENTS in python are used to perform CONTROL FLOW
#they check if a CONDITION is True or False and run the code INDENTED inside of them only if the CONDITION is True
#To create an IF STATEMENT write the word if, a boolean value, a variable that contains a boolean value or (most commonly) an expression that evaluates to a boolean value
#then end the line with a colon
#after the colon, you must write at least one INDENTed line of code
#an INDENTed line of code is a line that begins with whitespace (tabs or spaces)
#all consecutive of code at the same or greater level of INDENTATION (beginning with the same number of tabs or spaces)
#are considered to be inside the IF STATEMENT
#increasing the level of INDENTATION for no reason causes a syntax error
#to end the block of code inside the if statement, return to the previous level of INDENTATION
#(write a line of code with the same number of tabs or spaces in front of it (often 0) as the start of the if statement)
#IF STATEMENTS are typically used when the value of a variable is not known or certain and we want our program to respond appropriately to several differen values
#IF STATEMENTS (and other control flow blocks) can be NESTED inside of each other, an IF STATEMENTS inside of an IF STATEMENTS will only run the code inside of it if both of the IF STATEMENTS CONDITIONS are True
#An IF STATEMENT inside of an IF STATEMENT inside of an IF STATEMENT will only run the code inside of it if all three of the conditions are True!
#Exercise, using the code below as an example, ask your user several questions using and use IF STATEMENTs and COMPARISON OPERATORS to respond appropriately to different possible answers


name = input("What's your name?: ")
day = input(name+ " how's your day been?")
if day == "good":
    print("I'm really glad you're having a good day. My day's been good too")
    
if not day == "good": #the not operator inverts the boolean after it, not True results in a value of False, not False results in a value of True
    print("I'm sorry to hear that, my day's been pretty good.")
    
food = input("Serious question "+name+": what's your favourite food and is it pizza: ")
if food == "pizza":
    print("Mine too :D")
    best_friends = input("Want to be best friends")
    if best_friends == "yes":
        if input("really: ") == "really":
            if input("really really : ") == "really really":
                if input("really really really: ") == "really really really really really":
                    print("YAYYYYY!!!! ")
                    print("We're best friends now",name,":D")
                    print("Have some of my pizza")
                    print("🍕"*23211)
    
    if not best_friends == "yes":
        print("Oh I was just joking anyway. Bye. See you never >:(")
