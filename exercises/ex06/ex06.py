# Variable declaration setting an integer of 10
types_of_people = 10
# f-string declaration with an embedded variable in it
x = f"There are {types_of_people} of people"

# String variable
binary = "binary"
# Another string variable
do_not = "don't"

# An f-string variable with two embedded variables 
y = f"Those who know {binary} and those who {do_not}"

# Prints x variable (with f-string and it's embedded variables)
print(x)
# Prints y variable (with f-string and it's embedded variables)
print(y)

# Prints f-string with f-string variable (and it's embedded variables)
print(f"I said: {x}")
# Prints f-string with f-string variable (and it's embedded variables)
print(f"I also said: {y}")

# Boolean declaration
hilarious = False
# A string declaration with a placeholder to be used for .format()
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints string declaration and uses .format() to apply the value of the placeholder to contain the boolean statement
print(joke_evaluation.format(hilarious))

# String declaration
w = "this is the left side of..."
# String declaration
e = "a string with a right side."

# Prints both strings together (string concatenation)
print(w + e)
