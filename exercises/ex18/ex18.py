def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print(f"I got nothin' for ya")

print_two("Axel", "Olsson")
print_two_again("Axel", "Olsson!")
print_one("First one!")
print_none()