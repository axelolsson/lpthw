# For example you can run this script with

# Second prompt: exercises/ex22/ex22_sample.txt
# Third prompt: exercises/ex22/ex22_in.txt
# Last prompt: exercises/ex22/ex22_out.txt

# Accept arguments to the script
from sys import argv
from os.path import exists # Not used but can be used to check if a file exists

script, first, second = argv

print("String")
text = "Another string"
print(text)
print(f"{text}")
anotherText = print("This is the text {}")
print(text.format(text))
# This is a comment
# I can also print multiple lines with escape characters, and no Zed
# I will not be listing all of them
print("This is on one line\nand this will be on another")
print(
    """
I can also just do this
Which works just as well
"""
)
print(
    """
\t * Of course a list is in order
\t * Do laundry
\t * Learn python
"""
)
# I can also accept user input
user_name = input("What's your name? >")

print(f"Hello, {user_name}")

# Strings can be combined using the print(f"{x} {y}") syntax, or with concatenation
x = "Hey "
y = "there"

print(x + y)

print(f"{first} and {second}")

print("Type the path to the filename")
filename = input("> ")
txt = open(filename)

print(f"Here's the file")
print(txt.read())

# Don't forget to close
txt.close()

print("Type the path to the filename you want to create")
filename = input("> ")

print("Opening the file...")
target = open(filename, "w")

# Move file header to start of file and remove all the contents of the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

lines = f"""
{line1}
{line2}
{line3}
"""

target.write(lines)

print("And finally we, we close it.")
target.close()

print("Type the path to the filename you want to copy")
filename = input("> ")

print("Opening the file...")
from_file = open(filename).read()

# I can also copy from files (as long as the file exists)
print("Type the path to the filename you want to copy to")
filename = input("> ")

out_file = open(filename, "w")
out_file.write(from_file)

print("Alright, well done")

out_file.close()

# I can define functions and run them, and create functions that use other functions
def add(a, b):
  print(f"ADDING {a} + {b}")
  return a + b

def subtract(a, b):
  print(f"SUBTRACTING {a} - {b}")
  return a - b

sum = add(5, (subtract(5, 10)))

print(f"And the sum for that will be {sum}")