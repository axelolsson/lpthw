from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL (^C).")
print("If you do want that, hit RETURN.")

input("?")

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

print("Type the filename again")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())

txt_again.close()