# Print string
print("Mary had a little lamb.")
# Print string use format to set value of placeholder
print("Its fleece was white as {}.".format("snow"))
# Print string
print("And everywhere that Mary went.")
# Print string value ten times
print("." * 10) # Prints 10 dots

# String variable delcarations
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Concatenate string variables up to and including end6, then add a space
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
# Concatenate string variables from end7 up to and including end12
print(end7 + end8 + end9 + end10 + end11 + end12)

# Lines above prints Cheese Burger in the current format

# Lines below prints 
# Cheese
# Burger
print(end1 + end2 + end3 + end4 + end5 + end6,)
print(end7 + end8 + end9 + end10 + end11 + end12)