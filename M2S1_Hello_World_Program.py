print("Hello World!")

#function_name(argument)

print("Hello, Python!")
print('Guy')
print("Guy")
#print(Guy) - NameError - Guy is not defined
#print"Guy" - SyntaxError - Missing parentheses
#print("Guy") print("Walton") - SyntaxError - Invalid syntax
print("Guy","Walton")

#There cannot be more than one instruction on each line

print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")
print()
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

#The backslash (\) has a very special meaning when used inside strings
#this is called the escape character
#1. If you want to put just one backslash inside a string
#don't forget its escaping nature
#you have to double it.
#2. Not all escape pairs (the backslash coupled with another character) mean something.

#You can print multiple arguments within a single print function
#a print() function invoked with more than one argument outputs them all on one line;
#the print() function puts a space between the outputted arguments on its own initiative.

print("The itsy bitsy spider","climbed up","the water spout")

print("My name is", "Python.")
print("Monty Python.")

#The print() function has two keyword arguments that you can use for your purposes. The first is called end.
#a keyword argument consists of three elements: a keyword identifying the argument (end here); an equal sign (=); and a value assigned to that argument;
#any keyword arguments have to be put after the last positional argument (this is very important)
#In our example, we have made use of the end keyword argument, and set it to a string containing one space.

print("My name is", "Python.", end=" ")
print("Monty Python.")

#As you can see, the end keyword argument determines the characters the print() function sends to the output once it reaches the end of its positional arguments.
#The default behavior reflects the situation where the end keyword argument is implicitly used in the following way: end="\n".

print("My name is ", end="")
print("Monty Python.")

#As the end argument has been set to nothing, the print() function outputs nothing too, once its positional arguments have been exhausted.
#Note: no newlines have been sent to the output.

#We said previously that the print() function separates its outputted arguments with spaces. This behavior can be changed, too.
#The keyword argument that can do this is named sep (as in separator).

print("My", "name", "is", "Monty", "Python.", sep="-")

#The print() function now uses a dash, instead of a space, to separate the outputted arguments.
#Note: the sep argument's value may be an empty string, too.

#Both keyword arguments may be mixed in one invocation

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#The example doesn't make much sense, but it visibly presents the interactions between end and sep.

#2.12 - Scenario
#Modify the first line of code in the editor, using the sep and end keywords, to match the expected output. Use the two print() functions in the editor.
#Don't change anything in the second print() invocation.

print("Programming","Essentials","in")
print("Python")

#2.12 - Solution
print("Programming","Essentials","in",sep="***", end="...")
print("Python")

#2.13 - Scenario
#We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments. Feel free to modify any part of the code, but there is one condition ‒ learn from your mistakes and draw your own conclusions.

#Try to:
#minimize the number of print() function invocations by inserting the \n sequence into the strings;
#make the arrow twice as large (but keep the proportions)
#duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
#remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error ‒ is this the place where the error really exists?
#do the same with some of the parentheses;
#change any of the print words into something else, differing only in case (e.g., Print) ‒ what happens now?
#replace some of the quotes with apostrophes; watch what happens carefully.

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#2.13 - Solutions
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")

print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)

#Missing quote
"""print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***)
print("  *   *")
print("  *   *")
print("  *****")
"""

#Missing parenthesis
"""
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***"
print("  *   *")
print("  *   *")
print("  *****")
"""

#print must be lowercase
"""
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
Print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
"""

#Can use ' ' pr " " as long as they are used consistently
"""
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print('***   ***')
print("  *   *")
print( *   *")
print("  *****")
"""

#Summary
"""
1. The print() function is a built-in function. It prints/outputs a specified message to the screen/console window.

2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported. Python 3.8 comes with 69 built-in functions. You can find their full list provided in alphabetical order in the Python Standard Library.

3. To call a function (this process is known as function invocation or function call), you need to use the function name followed by parentheses. You can pass arguments into a function by placing them inside the parentheses. You must separate arguments with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen.

4. Python strings are delimited with quotes, e.g., "I am a string" (double quotes), or 'I am a string, too' (single quotes).

5. Computer programs are collections of instructions. An instruction is a command to perform a specific task when executed, e.g., to print a certain message to the screen.


6. In Python strings the backslash (\) is a special character which announces that the next character has a different meaning, e.g., \n (the newline character) starts a new output line.

7. Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted after the first, the third is outputted after the second, etc.

8. Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used to identify them.

9. The end and sep parameters can be used for formatting the output of the print() function. The sep parameter specifies the separator between the outputted arguments, e.g., print("H", "E", "L", "L", "O", sep="-"), whereas the end parameter specifies what to print at the end of the print statement.
"""